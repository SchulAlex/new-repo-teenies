from flask import render_template, request, redirect, url_for
from .forms import StoryForm, PollForm
from .models import Story, Poll, PollOption, PollVote
from . import db
from flask import current_app as app


@app.route('/')
def index():
    stories = Story.query.all()
    return render_template('index.html', stories=stories)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/story/new', methods=['GET', 'POST'])
def new_story():
    form = StoryForm()
    if form.validate_on_submit():
        story = Story(title=form.title.data, content=form.content.data)
        db.session.add(story)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_story.html', form=form)


@app.route('/polls', methods=['GET', 'POST'])
def polls():
    form = PollForm()
    if form.validate_on_submit():
        poll = Poll(question=form.question.data)
        db.session.add(poll)
        db.session.commit()
        for option in form.options.data:
            poll_option = PollOption(poll_id=poll.id, option_text=option)
            db.session.add(poll_option)
        db.session.commit()
        return redirect(url_for('polls'))
    return render_template('polls.html', form=form)


@app.route('/poll/<int:poll_id>', methods=['GET', 'POST'])
def poll_detail(poll_id):
    poll = Poll.query.get_or_404(poll_id)
    if request.method == 'POST':
        selected_option = request.form.get('option')
        vote = PollVote(poll_id=poll.id, option_id=selected_option)
        db.session.add(vote)
        db.session.commit()
        return redirect(url_for('poll_detail', poll_id=poll.id))
    return render_template('poll_detail.html', poll=poll)
