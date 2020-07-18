from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .models import Profile, FriendRequest, Comment, Discussion, DiscussionGroup, Event

class ModelInstantiationTests(TestCase):
    """
    Models are created exclusively in the backend side of things.
    This case of tests is designed to ensure that model
    instantiation is conducted as expected.

    ...

    Unit Tests
    ----------
    test_profile_instantiation
    test_friendrequest_instantiation
    test_comment_instantiation
    test_discussion_instantiation
    test_discussiongroup_instantiation
    test_event_instantiation
    """

    def test_profile_instantiation(self):
        """
        TODO
        """

        pass

    def test_friendrequest_instantiation(self):
        """
        TODO
        """

        pass

    def test_comment_instantiation(self):
        """
        TODO
        """

        pass

    def test_discussion_instantiation(self):
        """
        TODO
        """

        pass

    def test_discussiongroup_instantiation(self):
        """
        TODO
        """

        pass

    def test_event_instantiation(self):
        """
        TODO
        """

        pass

class ModelFunctionalTests(TestCase):
    """
    Most Model-to-Model interactions are performed exclusively in the
    backend of things. This case of unit tests make sure that model
    functionalities (other than instantiation) are good to go.

    ...

    Unit Tests
    ----------
    test_friendrequests
    """

    def test_friendrequests(self):
        """
        TODO
        """

        pass

class ModelViewTests(TestCase):
    """
    TODO
    """

    def test_profile_view(self):
        """
        TODO
        """

        pass
