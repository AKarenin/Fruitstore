from django.contrib import admin

from .models import FruitStore, FruitMenu

admin.site.register(FruitStore)
admin.site.register(FruitMenu)