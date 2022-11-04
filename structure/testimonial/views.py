from flask import render_template,url_for,flash, redirect,request,Blueprint
from flask_login import current_user,login_required
from structure import db
from structure.models import WebFeature,Testimonial
from structure.testimonial.forms import TestimonialForm

testimonials = Blueprint('testimonials',__name__)

@testimonials.route('/create_testimonial',methods=['GET','POST'])
@login_required
def create_testimonial():
    form = TestimonialForm()

    if form.validate_on_submit():

        testimonial = Testimonial(
        name=form.name.data,
        company=form.company.data,
        text=form.text.data,
        rating=form.rating.data,
                             )
        db.session.add(testimonial)
        db.session.commit()
        flash("Pricing Created")
        return redirect(request.args.get('next') or request.referrer )

    return render_template('create_testimonial.html',form=form)


# # int: makes sure that the testimonial_id gets passed as in integer
# # instead of a string so we can look it up later.
@testimonials.route('/<int:testimonial_id>')
def testimonial(testimonial_id):
    # grab the requested blog post by id number or return 404
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    return render_template('testimonial.html',name=testimonial.name,company=testimonial.company,text=testimonial.text,rating=testimonial.rating)
    
    

@testimonials.route("/<int:testimonial_id>/updatetestimonial", methods=['GET', 'POST'])
@login_required
def updatetestimonial(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)

    form = TestimonialForm()
    if request.method == 'POST':
        testimonial.name = form.name.data
        testimonial.company = form.company.data
        testimonial.text = form.text.data
        testimonial.rating = form.rating.data
        db.session.commit()
        flash('Post Updated')
        return redirect(request.args.get('next') or request.referrer )
    # Pass back the old blog post information so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.name.data = testimonial.name
        form.company.data = testimonial.company
        form.text.data = testimonial.text
        form.rating.data = testimonial.rating
    return render_template('updatetestimonial.html',
                           form=form,testimonial=testimonial)


@testimonials.route("/<int:testimonial_id>/updatet", methods=['GET', 'POST'])
@login_required
def updatet(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)

    form = TestimonialForm()
    if form.validate_on_submit():
        testimonial.name = form.name.data
        testimonial.company = form.company.data
        testimonial.text = form.text.data
        testimonial.rating = form.rating.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('core.index', testimonial_id=testimonial.id))
    # Pass back the old blog post information so they can start again with
    # the old text and title.
    elif request.method == 'GET':
        form.name.data = testimonial.name
        form.company.data = testimonial.company
        form.text.data = testimonial.text
        form.rating.data = testimonial.rating
    return redirect(url_for('core.editui'))





@testimonials.route("/testimonials", methods=['GET', 'POST'])
@login_required
def alltestimonials():

    testimonial = Testimonial.query.all()

    if testimonial:
        question = testimonial.question
        answer = testimonial.answer
        return render_template('base2.html', question=question, answer=answer,testimonial=testimonial)

   


@testimonials.route("/<int:testimonial_id>/delete_testimonial", methods=['POST','GET'])
@login_required
def delete_testimonial(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('core.index'))
