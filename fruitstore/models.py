from django.db import models



#배달 업체
#음식메뉴
#FruitStore

#FruitStore <1-1> 배달업체 (OneToOneField)
#FruitStore <1-n> 음식메뉴 (ForeignKey)
#FruitStore <n-m> ??? (ManyToManyField)

class FruitStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phoneNumber = models.IntegerField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.name}"

class FruitMenu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    fruitStore = models.ForeignKey(FruitStore, on_delete=models.CASCADE, related_name='fruitMenus')

    def __str__(self):
        return f"{self.name}"

