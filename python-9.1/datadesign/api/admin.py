from django.contrib import admin

from api.models import User, Agent, Event, Group, GroupUser

admin.site.register(User)

admin.site.register(Agent)

admin.site.register(Event)

admin.site.register(Group)

admin.site.register(GroupUser)