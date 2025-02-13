from django.db import models

#here's a way to register a new member to our system
class Membre (models.Model) :
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    given_name = models.CharField(max_length=150)
    birth = models.DateField()
    address = models.CharField(max_length=300)
    number = models.PositiveIntegerField()
    bio = models.TextField()
    date_acquired = models.DateTimeField(auto_now_add=True)
    money_GIVE = models.PositiveBigIntegerField()
    children = models.PositiveBigIntegerField()
    infos_children = models.TextField()
    spouse = models.CharField(max_length=150)
    statut_choices = [
           ('MARIE' , 'marié'),
        ('CELIBATAIRE' , 'celibataire'),
           ('VEUVE' , 'veuve'),
    ]
    statut = models.CharField(max_length=11, choices=statut_choices, default='VEUVE')

    def __str__(self):
        return f"  {self.name} {self.last_name} {self.given_name} "
class Space (models.Model):
    title = models.CharField(max_length=150, unique=True, default="")
    name = models.TextField()
    size = models.CharField(max_length=100)

    def __str__(self):
        return f" {self.name} {self.size}  "
    

class Propriete (models.Model):
    user = models.ForeignKey(Membre, on_delete=models.CASCADE, related_name='propriete')
    space =  models.OneToOneField(Space, related_name='spaces', on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.user.name} {self.user.given_name} {self.space.name} {self.space.size} "
    
class Appointment(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    given_name = models.CharField(max_length=150)
    number = models.PositiveBigIntegerField()
    date = models.DateTimeField()
    created_at  =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"  {self.name}  {self.last_name} {self.given_name} {self.date} "
    
class Receipt(models.Model):
    user = models.ForeignKey(Membre, on_delete=models.CASCADE, default="")
    title = models.CharField(max_length=150)
    price = models.PositiveBigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.user.name} {self.user.given_name} {self.title} {self.price} {self.created_at} "