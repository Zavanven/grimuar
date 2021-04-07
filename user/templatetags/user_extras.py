from django import template

register = template.Library()

# Custom tag to check if user is in group
@register.filter('in_group')
def in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()