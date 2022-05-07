from django.shortcuts import render
from profiles.models import Profile
from .models import Post
from django.db.models import Q


def posts_of_following_profile(request):
    # get logged user profile
    profile = Profile.objects.get(user=request.user)
    # check who we are following
    users = [user for user in profile.following.all()]

    # initaial values for variable
    posts = []
    qs = None
    # get the people who we are following
    for u in users:
        p = Profile.objects.get(user=u)
        # p = Profile.objects.filter(user=u)
        p_post = p.post_set.all()
        posts.append(p_post)
    # our post
    my_post = profile.profile_post()
    posts.append(my_post)
    return render(request, 'post/main.html', {'post': posts})