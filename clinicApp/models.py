from django.db import models


# Create your models here.
#Contact
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.PositiveIntegerField()
    email = models.EmailField()
    localisation = models.CharField(max_length=100)

    def __str__(self):
        return self.email


#A propos
class About(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.description



#Actualité
class New(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, default="Titre de lactualité")
    image = models.ImageField(upload_to='news/%Y/%m/%d/',null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
#categorie
class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, default="Titre de la categorie")
    def __str__(self):
        return self.title
#service
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, default="Titre du service")
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.title
#appreciation
class Appreciation(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=400, default="Titre de la categorie")
    WHAT=(
        ('suggestion','suggestion'),
        ('comment','commentaire'),
    )
    type = models.CharField(max_length=11,choices = WHAT)
    def __str__(self):
        return self.content
#rendez-vous
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    customerFirstName = models.CharField(max_length=50,default="Prenom")
    customerLastName = models.CharField(max_length=15,default="Nom")
    customerEmail = models.EmailField(max_length=50,default="Email@emailcom")
    doctor = models.CharField(max_length=50,default="Docteur")
    customerNumber = models.CharField(max_length=50,default="Numero")
    hour = models.DateTimeField('Heure',blank=True,null=True)
    service = models.OneToOneField(
        Service,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.customerEmail
