from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired
from structure.models import Appearance

appearance = Appearance.query.all()
class AppearanceForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    # text_color field with red, green, blue, white, black, yellow, orange, purple, pink, brown, grey, and dark grey options
    title_color = SelectField('Text Color', choices=[('select','Select'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('grey', 'Grey'), ('dark grey', 'Dark Grey')],default=[])
    # subtitle_color field with red, green, blue, white, black, yellow, orange, purple, pink, brown, grey, and dark grey options
    subtitle_color = SelectField('Subtitle Color', choices=[('select','Select'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('grey', 'Grey'), ('dark grey', 'Dark Grey')],default='')
    # paragraph_color field with red, green, blue, white, black, yellow, orange, purple, pink, brown, grey, and dark grey options
    paragraph_color = SelectField('Paragraph Color', choices=[('select','Select'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), ('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('grey', 'Grey'), ('dark grey', 'Dark Grey')],default='')
    #title_font field with Arial, Times New Roman, Georgia, Verdana, Helvetica, and Impact options
    title_font = SelectField('Title Font', choices=[('select','Select'),('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Impact', 'Impact')],default='')
    #subtitle_font field with Arial, Times New Roman, Georgia, Verdana, Helvetica, and Impact options
    subtitle_font = SelectField('Subtitle Font', choices=[('select','Select'),('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Impact', 'Impact')],default='')
    #paragraph_font field with Arial, Times New Roman, Georgia, Verdana, Helvetica, and Impact options
    paragraph_font = SelectField('Paragraph Font', choices=[('select','Select'),('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Impact', 'Impact')],default='')
    #title_size field with 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, and 34 options
    title_size = SelectField('Title Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')    ],default='')
    #subtitle_size field with 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, and 34 options
    title_size = SelectField('Title Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')    ],default='')
    subtitle_size = SelectField('Subtitle Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')    ])
    #paragraph_size field with 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, and 34 options
    title_size = SelectField('Title Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')    ],default='')
    paragraph_size = SelectField('Paragraph Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')    ],default='')
    bootstrap_class1= SelectField('Bootstrap Class 1', choices=[('select','Select'),('col-md-4', 'col-md-4'), ('col-md-6', 'col-md-6'), ('col-md-8', 'col-md-8'), ('col-md-10', 'col-md-10'), ('col-md-12', 'col-md-12')])
    bootstrap_class2= SelectField('Bootstrap Class 2', choices=[('select','Select'),('col-md-4', 'col-md-4'), ('col-md-6', 'col-md-6'), ('col-md-8', 'col-md-8'), ('col-md-10', 'col-md-10'), ('col-md-12', 'col-md-12')])
    bootstrap_class3= SelectField('Bootstrap Class 3', choices=[('select','Select'),('col-md-4', 'col-md-4'), ('col-md-6', 'col-md-6'), ('col-md-8', 'col-md-8'), ('col-md-10', 'col-md-10'), ('col-md-12', 'col-md-12')])

    submit = SubmitField('SUBMIT')




#loop through Appearance model and create a form for each appearance with default values from
for appearance in Appearance.query.all():
    class AppearanceForm1(FlaskForm):
        title_color = SelectField('Text Color', choices=[('select','Select'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'), 
        ('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), 
        ('brown', 'Brown'), ('grey', 'Grey'), ('dark grey', 'Dark Grey')], default=appearance.title_color)
        subtitle_color = SelectField('Subtitle Color', choices=[('select','Select'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'),
        ('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'),
        ('brown', 'Brown'), ('grey', 'Grey'), ('dark grey', 'Dark Grey')], default=appearance.subtitle_color)
        paragraph_color = SelectField('Paragraph Color', choices=[('select','Select'),('red', 'Red'), ('green', 'Green'), ('blue', 'Blue'),
        ('white', 'White'), ('black', 'Black'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'),
        ('brown', 'Brown'), ('grey', 'Grey'), ('dark grey', 'Dark Grey')], default=appearance.paragraph_color)
        title_font = SelectField('Title Font', choices=[('select','Select'),('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Impact', 'Impact')], default=appearance.title_font)
        subtitle_font = SelectField('Subtitle Font', choices=[('select','Select'),('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Impact', 'Impact')], default=appearance.subtitle_font)
        paragraph_font = SelectField('Paragraph Font', choices=[('select','Select'),('Arial', 'Arial'), ('Times New Roman', 'Times New Roman'), ('Georgia', 'Georgia'), ('Verdana', 'Verdana'), ('Helvetica', 'Helvetica'), ('Impact', 'Impact')], default=appearance.paragraph_font)
        title_size = SelectField('Title Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')], default=appearance.title_size)
        subtitle_size = SelectField('Subtitle Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')], default=appearance.subtitle_size)
        paragraph_size = SelectField('Paragraph Size', choices=[('select','Select'),('12','12'),('14','14'),('16','16'),('18','18')], default=appearance.paragraph_size)
        bootstrap_class1= SelectField('Bootstrap Class 1', choices=[('select','Select'),('col-md-4', 'col-md-4'), ('col-md-6', 'col-md-6'), ('col-md-8', 'col-md-8'), ('col-md-10', 'col-md-10'), ('col-md-12', 'col-md-12')], default=appearance.bootstrap_class1)
        bootstrap_class2= SelectField('Bootstrap Class 2', choices=[('select','Select'),('col-md-4', 'col-md-4'), ('col-md-6', 'col-md-6'), ('col-md-8', 'col-md-8'), ('col-md-10', 'col-md-10'), ('col-md-12', 'col-md-12')], default=appearance.bootstrap_class2)
        bootstrap_class3= SelectField('Bootstrap Class 3', choices=[('select','Select'),('col-md-4', 'col-md-4'), ('col-md-6', 'col-md-6'), ('col-md-8', 'col-md-8'), ('col-md-10', 'col-md-10'), ('col-md-12', 'col-md-12')], default=appearance.bootstrap_class3)
        submit = SubmitField('SUBMIT')
        