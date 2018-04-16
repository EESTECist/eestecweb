from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import ExtendedUser, Team, MotivationLetters
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.urls import reverse
from .forms import UserForm, UserLoginForm, TeamForm


def register(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'user/register.html', context={'form': form})

    elif request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            image = request.FILES['image']
            bio = request.POST['bio']
        except:
            return HttpResponseRedirect('/user/asd/')

        ExtendedUser.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, image=image, bio=bio)
        return HttpResponseRedirect('/user/login/')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/login.html', context={'form': UserLoginForm()})
    elif request.method == 'POST':
        # authenticate
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponseRedirect('/user/login/')

        login(request, user)

        return HttpResponseRedirect('/home/')


class TeamCreateView(CreateView):
    form_class = TeamForm
    queryset = Team.objects.all()
    template_name = 'user/create_team.html'

    def form_valid(self, form):
        if self.request.user.is_yk:
            form.instance.president = self.request.user
            self.object = form.save()

            return super(TeamCreateView, self).form_valid(form)

        return self.form_invalid(form)


class TeamPageView(DetailView):
    queryset = Team.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    template_name = 'user/team_detail.html'
    context_object_name = 'team'


def join(request, team_slug):
    team = get_object_or_404(Team, slug=team_slug)
    if request.user not in [u for u in team.members.all()]:
        motivation_letter = request.POST['letter']
        new_letter = MotivationLetters()
        new_letter.team = team
        new_letter.author = request.user
        new_letter.letter = motivation_letter

        new_letter.save()

        return HttpResponseRedirect(new_letter.get_absolute_url())

    return HttpResponseRedirect(MotivationLetters.get_absolute_url())


class InvestigateLetters(ListView):
    queryset = MotivationLetters.objects.all()
    context_object_name = 'letter'
    paginator_class = Paginator
    paginate_by = 10

    def get_team(self):
        slug = self.kwargs['slug']
        team = get_object_or_404(Team, slug=slug)
        return team

    def get_queryset(self):
        team = self.get_team()
        return team.motivationletters_set.all()

    def get_context_data(self, **kwargs):
        context = super(InvestigateLetters, self).get_context_data(**kwargs)
        for data in context:
            data['approve_url'] = reverse('user:approve', kwargs={'user': self.request.user.id, 'team': data.team.slug})

        return context

    def get(self, request, *args, **kwargs):
        team = self.get_team()
        if request.user == team.president:
            return super(InvestigateLetters, self).get(request, *args, **kwargs)

        return HttpResponseRedirect('/home/')


def approve(request, user, team):
    user = get_object_or_404(ExtendedUser, id=user)
    team = get_object_or_404(Team, slug=team)

    if team.president == request.user:
        if user not in team.members.all():
            team.members.add(user)
            team.save()

            return JsonResponse({'success': 'member joined'})

        else:
            return JsonResponse({'error': 'user is already a member'})

    return JsonResponse({'error': 'unauthorized attempt'})


