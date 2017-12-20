import os
from django import template
from forum.models import Post

register = template.Library()

@register.simple_tag
def grade(post, user_id):
    return post.get_grade_string(user_id)
