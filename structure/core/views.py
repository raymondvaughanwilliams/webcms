from flask import render_template,request,Blueprint,redirect,url_for
from structure.models import User,About,Price, WebFeature,Faq,Testimonial,Team,Appearance,Block,app
# from structure.team.views import team
from structure.web_features.forms import WebFeatureForm
from structure.team.forms import UpdateTeamForm
from structure.about.forms import UpdateAboutForm
from structure.faq.forms import FaqForm
from structure.pricing.forms import PriceForm
from structure.testimonial.forms import TestimonialForm
from structure.about.forms import AboutForm
from structure.block.forms import BlockForm
from sqlalchemy.orm import load_only
from flask_login import login_required
from structure.appearance.forms import AppearanceForm
from structure.block.forms import BlockForm
from structure.appearance.views import appearance
from structure.models import Appearance
from structure.core.forms import ContactForm
from flask_mail import Message,Mail 
core = Blueprint('core',__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "raymondvaughanwilliams@gmail.com"
app.config["MAIL_PASSWORD"] = "mowfdigzaouywugg"


@core.route('/dash')
@login_required
def index():
    '''
    This is the home page view. Notice how it uses pagination to show a limited
    number of posts by limiting its query size and then calling paginate.
    '''
    page = request.args.get('page', 1, type=int)
    about = About.query.get(1)
    faq = Faq.query.all()
    team = Team.query.all()
    pricing = Price.query.all()
    testimonial = Testimonial.query.all()
    feature_count = WebFeature.query.count()
    faq_count = Faq.query.count()
    team_count = Team.query.count()
    pricing_count = Price.query.count()
    testimonial_count = Testimonial.query.count()
    web_features = WebFeature.query.order_by(WebFeature.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html',web_features=web_features,about=about,faq=faq,team=team,pricing=pricing,testimonial=testimonial,feature_count=feature_count,faq_count=faq_count,team_count=team_count,pricing_count=pricing_count,testimonial_count=testimonial_count)

@core.route('/base')
def base():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    about = About.query.all()
    return render_template('base.html',about=about)


@core.route('/')
def hmsui():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    form = ContactForm()

    page = request.args.get('page', 1, type=int)
    web_features = WebFeature.query.filter_by(mainpage="yes").order_by(WebFeature.date.desc()).paginate(page=page, per_page=10)
    about = About.query.get(1)
    price = Price.query.all()
    faq = Faq.query.all()
    testimonial = Testimonial.query.all()
    team= Team.query.all()
    serv = Price.features
    Blockform= BlockForm()
    team= Team.query.all()
    block= Block.query.all()
    Appearanceform = AppearanceForm()
    appearance=Appearance.query.all()
    # services=[]
    # service= serv.split(',')
    # services.append(service)
    return render_template('main.html',web_features=web_features, about=about,pricing=price,faq=faq,testimonial=testimonial,team=team,serv=serv,Blockform=Blockform,appearance=appearance,Appearanceform=Appearanceform,block=block,form=form)







@core.route('/editui')
@login_required
def editui():
    '''
    Example view of any other "core" page. Such as a info page, about page,
    contact page. Any page that doesn't really sync with one of the models.
    '''
    Webfeatureform= WebFeatureForm()
    Teammateform = UpdateTeamForm()
    Faqform = FaqForm() 
    Testimonialform = TestimonialForm()
    Pricingform = PriceForm()
    Aboutform = AboutForm()
    page = request.args.get('page', 1, type=int)
    web_features = WebFeature.query.order_by(WebFeature.date.desc()).paginate(page=page, per_page=10)
    about = About.query.get(1)
    price = Price.query.all()
    faq = Faq.query.all()
    Blockform= BlockForm()
    testimonial = Testimonial.query.all()
    team= Team.query.all()
    block= Block.query.all()
    Appearanceform = AppearanceForm()
    appearance=Appearance.query.all()
    appearancef=Appearance.query.filter_by(id=1).first()
    if request.method == 'GET':
        Appearanceform.title_color.data = appearancef.title_color
        Appearanceform.subtitle_color.data = appearancef.subtitle_color
        Appearanceform.paragraph_color.data = appearancef.paragraph_color
        Appearanceform.title_font.data = appearancef.title_font
        Appearanceform.subtitle_font.data = appearancef.subtitle_font
        Appearanceform.paragraph_font.data = appearancef.paragraph_font
        Appearanceform.title_size.data = appearancef.title_size
        Appearanceform.subtitle_size.data = appearancef.subtitle_size
        Appearanceform.paragraph_size.data = appearancef.paragraph_size
        Appearanceform.bootstrap_class1.data = appearancef.bootstrap_class1
        Appearanceform.bootstrap_class2.data = appearancef.bootstrap_class2
        Appearanceform.bootstrap_class3.data = appearancef.bootstrap_class3

    # for appearances in appearance:
    #         appearance=Appearance.query.all()
    #         Appearanceform = AppearanceForm()
    #         Appearanceform.title_color.data = appearances.title_color
    #         Appearanceform.subtitle_color.data = appearances.subtitle_color
    #         Appearanceform.paragraph_color.data = appearances.paragraph_color
    #         Appearanceform.title_font.data = appearances.title_font
    #         Appearanceform.subtitle_font.data = appearances.subtitle_font
    #         Appearanceform.paragraph_font.data = appearances.paragraph_font
    #         Appearanceform.title_size.data = appearances.title_size
    #         Appearanceform.subtitle_size.data = appearances.subtitle_size
    #         Appearanceform.paragraph_size.data = appearances.paragraph_size
    #         Appearanceform.bootstrap_class1.data = appearances.bootstrap_class1
    #         Appearanceform.bootstrap_class2.data = appearances.bootstrap_class2
    #         Appearanceform.bootstrap_class3.data = appearances.bootstrap_class3


    # fields = ['id']
    # data = Testimonial.options(load_only(*fields)).all()
    emplist = []
    for faqs in faq:
        emplist.append("row:" +str(faqs.id))
    print(emplist)


    templist = []
    for testimonials in testimonial:
        templist= "row:" +str(testimonials.id)
    #     templist.append("row:" +str(testimonials.id))
    # print(templist)



    print(faq)
    context={
        'about':about,
        'web_features':web_features,
        'price':price,
        'faq':faq,
        'testimonial':testimonial,
        'team':team,
    }

    serv = Price.features
    # services=[]
    # service= serv.split(',')
    # services.append(service)
    return render_template('editui.html',block = block,web_features=web_features,appearancef =appearancef,about=about,webfeatureform = Webfeatureform,teammateform=Teammateform,faqform = Faqform,testimonialform=Testimonialform,priceform=Pricingform,aboutform=Aboutform,team=team,pricing=price,faq=faq,testimonial=testimonial,templist=templist,emplist=emplist,blockform=Blockform,appearanceform=Appearanceform,appearance=appearance)
    # return render_template('info.html',context=context,faq=faq)



@core.route('/<int:web_feature_id>')
def web_feature(web_feature_id):
    about = About.query.get(1)
    form=ContactForm()

    # grab the requested blog post by id number or return 404
    web_feature = WebFeature.query.get_or_404(web_feature_id)
    return render_template('feature.html',title=web_feature.title,form=form,
                            date=web_feature.date,web_feature=web_feature,about=about,feature=web_feature
    )


@core.route('/features')
def features():
    features = WebFeature.query.all()
    about = About.query.get(1)
    form = ContactForm()
    return render_template('features.html',features=features,about=about,form=form)


@core.route('/contact-us',methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if request.method == 'POST':
        print("ajk")
  
        
        name = form.name.data
        text = form.text.data
        email = form.email.data
        
        # Send email using Flask-Mail
        # (Assuming Flask-Mail is configured and imported)
        mail = Mail(app)
        msg = Message('Contact Us Request',
                        sender=email,
                        recipients=['raymondvaughanwilliams@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {text}"
        mail.send(msg)
        return redirect(url_for('core.hmsui'))

            
