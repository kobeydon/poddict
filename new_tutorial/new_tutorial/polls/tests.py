
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.shortcuts import resolve_url
from .models import Question


# Create your tests here.
class PollsTest(TestCase):
    def test_was_publishedd_recently(self):
        obj = Question(pub_date=timezone.now())
        self.assertTrue(obj.was_published_recently(), 'published right now')

        obj = Question(pub_date=timezone.now() - timedelta(days=1, minutes=1))
        self.assertFalse(obj.was_published_recently(), 'Oneday and a minute old')

        obj = Question(pub_date=timezone.now() - timedelta(days=1) + timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), 'not quite Oneday old')

        obj = Question(pub_date=timezone.now() - timedelta(minutes=1))
        self.assertTrue(obj.was_published_recently(), 'a minite old')

        obj = Question(pub_date=timezone.now() + timedelta(minutes=1))
        self.assertFalse(obj.was_published_recently(), 'will be published a minute later')

class viewtest(TestCase):
    def test_index(self):
        response = self.client.get(resolve_url('polls:index'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.context['latest_question_list'].count())

        Question.objects.create(
            question_text='aaa',
            pub_date=timezone.now(),
        )
        response = self.client.get(resolve_url('polls:index'))
        self.assertEqual(1, response.context['latest_question_list'].count())

        self.assertEqual('aaa', response.context['latest_question_list'].first().question_text)
