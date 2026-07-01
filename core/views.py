from django.shortcuts import render


def portfolio(request):
	projects = [
		{
			"name": "TeamFlow",
			"description": "A workflow app for tracking tasks, habits, and team progress.",
			"stack": "Django, SQLite, Bootstrap",
		},
		{
			"name": "Habit Sprint",
			"description": "A focused habit tracker with streaks and weekly goals.",
			"stack": "Python, Django, JavaScript",
		},
		{
			"name": "Ops Dashboard",
			"description": "A clean internal dashboard for metrics and reporting.",
			"stack": "Django, Charts, SQL",
		},
	]

	skills = ["Python", "Django", "REST APIs", "SQLite", "HTML/CSS", "JavaScript"]

	return render(
		request,
		"core/portfolio.html",
		{
			"projects": projects,
			"skills": skills,
		},
	)
