from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Profile(models.Model):
    """
    Primary object for logging into the site.
    Extends the User object via one-to-one -connection.

    Attributes
    ----------
    user : User
        The User instance that the profile is connected to.
        Each Profile instance has a unique User instance.
    friend_list : List<Profile>
        List of other profiles that a profile is friends with.
        A profile cannot be a friend with itself.
    description : string
        A brief description of the Profile instance.
        Acts as a 'bio'.
    location : string
        The location of the profile that they have set.
    birthdate : datetime
        Date instance of the time of birth of the creator
        of the Profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Useful User Model attributes:
    # first_name
    # last_name
    # email
    # password
    # is_superuser
    # date_joined
    # last_login

    friend_list = models.ManyToManyField("self")
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=255, blank=False)
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Getter for string representation of the Profile instance.

        Returns
        -------
        string
            String representation of the Profile:
            '(ID = x) Profile: y', where
            x = Profile ID
            y = Profile Username
        """

        return "(ID = {}) Profile: {}".format(str(self.pk), self.user.username)

    def __eq__(self, other):
        """
        Function for comparing equality between two Profile instances.
        Equality is based on the primary key values of both Profile instances
        and the User instances that they are bound to.

        Returns
        -------
        bool
            True, if the Profile instances are determined to be
            the same. False otherwise.
        """

        if self.pk == other.pk and self.user.pk == other.user.pk:
            return True
        else:
            return False

    def check_friend_request(self, other):
        """
        Checks whether specified Profile has created a friend request
        for this instance.

        Parameters
        ----------
        other : Profile
            The Profile instance that potentially created
            a friend request.

        Returns
        -------
        FriendRequest
            Instance of subject friend request. If it does not exist,
            None is returned.
        """

        try:
            friend_request = FriendRequest.objects.get(sender=other, receiver=self)
            return friend_request
        except FriendRequest.DoesNotExist:
            return None

    def send_friend_request(self, other):
        """
        Creates a friendship request to specified user, letting
        them know of the proposal. If a friendship request with
        sender and receiver swapped exists, then, instead of
        creating a new friendship request, existing one is
        accepted.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        other : Profile
            Target Profile instance of the friendship request.
        """

        if check_friend_request(other) is not None:
            # Friend request with swapped recipients exists.
            # Instead of creating a new friend request, the
            # existing one is accpeted instead.
            accept_friend_request(other)
            return
        if self == other:
            # A Profile instance cannot be friends with itself.
            return
        try:
            # Start by checking whether target friend request
            # already exists.
            existing_request = FriendRequest.objects.get(sender=self, receiver=other)

            # Check the status of the request. There are 3 different states:
            # - True: Request was accepted.
            # - False: Request was declined.
            # - None: Request is yet to receive a response.
            if existing_request.status is False:
                # With the status set to False, the friend request has
                # been declined. It can be sent again after a week has passed.
                existing_date = existing_request.request_date
                threshold_date = existing_date + timedelta(days=7)
                if datetime.now() > threshold_date:
                    # Setting the status to "None" puts the request
                    # back into a "pending" state.
                    existing_request.set_status(None)
                    existing_request.save()
        except FriendRequest.DoesNotExist:
            # Target friend request does not exist.
            FriendRequest.objects.create(sender=self, receiver=other)

    def reject_friend_request(self, other):
        """
        Rejects a friend request sent by specified Profile.
        Does nothing if such a request does not exist.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        other : Profile
            The Profile instance that sent the friend request.
        """

        friend_request = self.check_friend_request(other)
        if friend_request is not None:
            friend_request.set_status(False)
            friend_request.save()

    def accept_friend_request(self, other):
        """
        Accepts a friend request sent by specified Profile.
        Upon accepting a friend request, additions to the
        friend lists are also conducted.
        Does nothing if such a request does not exist.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        other : Profile
            The Profile instance that sent the friend request.
        """

        friend_request = self.check_friend_request(other)
        if friend_request is not None:
            friend_request.set_status(True)
            friend_request.save()
            add_friend(other)

    def add_friend(self, other):
        """
        Adds specified Profile into the friend list.
        A Profile instance cannot be friends by itself.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        other : Profile
            The Profile instance that is to be added to the
            friend list.
        """

        if self == other:
            # A Profile instance cannot be friends with itself.
            return

        # Add Profile instances to both friend lists.
        self.friend_list.add(other)
        other.friend_list.add(self)
        self.save()
        other.save()

    def remove_friend(self, other):
        """
        Removes specified Profile from the friend list.
        Does nothing if specified Profile is not on the list.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        other : Profile
            The Profile instance that is to be removed from
            the friend list.
        """

        if self == other:
            # A Profile instance cannot be friends with itself.
            return

        # The friend request associated with the friendship is
        # maintained. Its status should be set to False.
        friend_request = self.check_friend_request(other)
        if friend_request is None:
            friend_request = other.check_friend_request(self)
            if friend_request is None:
                # Friend request does not exist. Aborting procedure.
                return

        friend_request.set_status(False)
        friend_request.save()

        # Remove Profile instances from both friend lists.
        self.friend_list.remove(other)
        other.friend_list.remove(self)
        self.save()
        other.save()


class FriendRequest(models.Model):
    """
    Connection instance for creating friendships between users.

    ...

    Attributes
    ----------
    sender : Profile
        The creator of the friend request.
    receiver : Profile
        The target of the friend request.
    request_date : datetime
        The time at which the friend request was created.
    status : bool
        Current state of the friend request:
        - True: Friend request was accepted.
        - False: Friend request was declined.
        - None: Friend request is pending.
    """

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    request_date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=None)

    def __str__(self):
        """
        Getter for string representation of the friend request.

        Returns
        -------
        string
            String representation of the friend request:
            '(ID = x) Friend Request - Sender / Receiver: y / z', where
            x = Friend Request ID
            y = Sender Profile
            z = Receiver Profile
        """
        return "(ID = {}) Friend Request - Sender / Receiver: {} / {}".format(str(self.pk), self.sender.user.username, other.sender.user.username)

class DiscussionGroup(models.Model):
    """
    Discussion-oriented group instance. Profiles can join these groups,
    be it public, passphrase-protected or invitation only.

    Attributes
    ----------
    title : string
        The topic of the group.
    description : string
        Further details relating to the topic of the group.
    creator : Profile
        Profile instance of the one who created the group.
    creation_date : datetime
        Time at which the group was created.
    participants : List<Profile>
        List of Profiles that are a part of the group.
    passphrase : string
        A phrase that a Profile has to provide in order to join
        the group. If this is blank, passphrase is not required.
    invitation_required : bool
        Determines whether a Profile can only join the group via
        an invitation.
    invitees : List<Profile>
        List of Profiles that have been invited to the group.
    """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    creator = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="profile_created_groups", blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    participants = models.ManyToManyField(Profile, related_name="profile_associated_groups")
    passphrase = models.CharField(max_length=50, blank=True)
    invitation_required = models.BooleanField(default=False)
    invitees = models.ManyToManyField(Profile, related_name="profile_group_invitations")

    def __str__(self):
        """
        Getter for string representation of the discussion group.

        Returns
        -------
        string
            String representation of the discussion group:
            '(ID = x) Discussion Group y, created by z at a', where
            x = Discussion Group ID
            y = Topic of the group
            z = Creator of the group (Profile username)
            a = Date of creation
        """

        return "(ID = {}) Discussion Group '{}', created by '{}' at {}".format(str(self.pk), self.title, self.creator.user.username, str(self.creation_date))

class Discussion(models.Model):
    """
    Instance of a discussion, between 2 or more Profiles, or related
    to a particular group.

    ...

    Attributes
    ----------
    title : string
        The topic of the discussion, displayed as a string.
    description : string
        Further details of the discussion, relating to its title.
    creator : Profile
        Profile instance of the user who created it.
    creation_date : datetime
        The time at which the discussion was created.
    related_group : DiscussionGroup
        A group that the discussion might be associated with.
        This can be None.
    """

    title = models.CharField(max_length=50, default="Unspecified Discussion Topic")
    description = models.CharField(max_length=255, blank=True, null=True)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_created_discussions")
    creation_date = models.DateTimeField(default=datetime.now, blank=True)
    related_group = models.ForeignKey(DiscussionGroup, on_delete=models.SET_NULL, related_name="group_discussions", blank=True, null=True)

    def __str__(self):
        """
        Getter for string representation of the Discussion.

        Returns
        -------
        string
            String representation of the Discussion:
            '(ID = x) Discussion subject: y, created by z at a', where
            x = Discussion ID
            y = Discussion Title
            z = Discussion Creator (Profile username)
            a = Time of creation
        """

        return "(ID = {}) Discussion subject: '{}', created by '{}' at '{}'".format(str(self.pk), self.title, self.creator.user.username, str(self.creation_date))

class Comment(models.Model):
    """
    Instance of feedback left behind by a User Profile on a
    discussion instance.

    ...

    Attributes
    ----------
    commenter : Profile
        The Profile instance that created the comment.
    creation_date : datetime
        The time at which the comment was created.
    edit_date : datetime
        The time at which the comment was most recently edited.
    contents : string
        The comment itself.
    related_discussion : Discussion
        The discussion that the comment is associated with.
    approval : int
        Integer rating of the comment.
    """

    commenter = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True, related_name="profile_comments")
    creation_date = models.DateTimeField(default=datetime.now)
    edit_date = models.DateTimeField(default=datetime.now)
    contents = models.CharField(max_length=255)
    related_discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, blank=True, null=True, related_name="discussion_comments")
    approval = models.IntegerField(default=0)

    def __str__(self):
        """
        Getter for string representation of the comment instance.

        Returns
        -------
        string
            String representation of the comment:
            '(ID = x) Comment by y at z', where
            x = Comment ID
            y = Profile Username
            z = Creation Date
        """

        return "(ID = {}) Comment by '{}' at '{}'".format(str(self.pk), self.commenter.user.username, str(self.creation_date))

    def edit_comment(self, new_comment):
        """
        Applies an edit to the comment, updating the edit date
        in the process.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        new_comment : string
            New contents of the comment.
        """

        self.contents = new_comment
        self.edit_date = datetime.now()
        self.save()

    def add_approval(self, approval_value):
        """
        Adds a vote of approval/disapproval to the comment.

        Saves any changes that have been made into the database.

        Parameters
        ----------
        approval_value : bool
            If True, approve of the comment (increment by 1).
            If False, disapprove of the comment (decrement by 1).

        Returns
        -------
        int
            Current approval rating of the comment after
            applying user approval.
        """

        if approval_value is True:
            self.approval = self.approval + 1
        else:
            self.approval = self.approval - 1

        self.save()
        return self.approval

class Event(models.Model):
    """
    Simple representation of an event, scheduled to take place in
    a specified location.

    ...

    Attributes
    ----------
    title : string
        Briefly describes the topic of the event.
    description : string
        Provides more details on the topic of the event.
    host : Profile
        Profile instance of the user who hosts the event.
    participants : List<Profile>
        List of people who are going to participate in the event.
    invitees : List<Profile>
        List of people who are specifically invited to the event.
        A Profile being on this list bypasses the 'private' flag
        for them.
    location : string
        The venue of the event.
    start_date : datetime
        Time at which the event will start.
    end_date : datetime
        Time at which the event will end.
    cancelled : bool
        Determines whether the event has been cancelled.
    private : bool
        Determines the availability of the event. If set to True,
        only friends of the host can participate. If set to False,
        anyone can participate.
    """

    title = models.CharField(max_length=50)
    description = models.TextField()
    host = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_hosted_events")
    participants = models.ManyToManyField(Profile, related_name="profile_attended_events")
    invitees = models.ManyToManyField(Profile, related_name="profile_event_invitations")
    location = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    cancelled = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        """
        Getter for string representation of the event.

        Returns
        -------
        string
            String representation of the event:
            '(ID = x) Event y, hosted by z', where
            x = Event ID
            y = Event Title
            z = Event Host (Profile username)
        """

        return "(ID = {}) Event '{}' in '{}', hosted by '{}'".format(str(self.pk), self.title, self.location, self.host.user.username)

# TODO: "thirdfloor Models"
# - Forum
# - ForumPost
# - PostVote
