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
    # The following details can be found from User Model:
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

        return "(ID = " + str(self.pk) + ") Profile: " + self.user.username

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

    def get_user(self):
        """
        Getter for the user instance of the Profile.

        Returns
        -------
        User
            User instance bound to the Profile.
        """

        return self.user

    def get_description(self):
        """
        Getter for the description of the Profile.

        Returns
        -------
        string
            Profile description.
        """

        return self.description

    def get_location(self):
        """
        Getter for the location of the Profile.

        Returns
        -------
        string
            String representation of the location of the creator
            of the Profile.
        """

        return self.location

    def get_birthdate(self):
        """
        Getter for the birth date of the creator of the Profile.

        Returns
        -------
        datetime
            Date of birth of the creator of the Profile.
        """

        return self.birthdate

    def set_description(self, desc):
        """
        Setter for the description of the Profile.
        Does not save the change to the database.

        Parameters
        ----------
        desc : string
            Target description for the Profile.
        """

        self.description = desc

    def set_location(self, loc):
        """
        Setter for the location of the Profile.
        Does not save the change to the database.

        Parameters
        ----------
        loc : string
            String representation of the location of the creator
            of the Profile.
        """

        self.location = loc

    def set_birthdate(self, date):
        """
        Setter for the birth date of the Profile.
        Does not save the change to the database.

        Parameters
        ----------
        date : datetime
            Date instance of the birth date of the creator
            of the Profile.
        """

        self.birthdate = date

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
        """

        if self == other:
            # A Profile instance cannot be friends with itself.
            return

        # The friend request associated with the friendship is
        # maintained. Its status should be set to False.
        friend_request = self.check_friend_request(other)
        if friend_request is None:
            friend_request = other.check_friend_request(self)
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

    sender = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="receiver")
    request_date = models.DateTimeField(default=datetime.now)
    status = models.BooleanField()

    def __str__(self):
        return "Friend Request - Sender / Receiver:" + self.sender.user.username + " / " self.receiver.user.username

    def get_sender(self):
        """
        Getter for the sender of the friend request.

        Returns
        -------
        Profile
            Profile instance of the creator of the friend request.
        """

        return self.sender

    def get_receiver(self):
        """
        Getter for the receiver of the friend request.

        Returns
        -------
        Profile
            Profile instance of the receiver of the friend request.
        """

        return self.receiver

    def get_request_date(self):
        """
        Getter for the date of the creation of the friend request.

        Returns
        -------
        datetime
            Date instance of the time at which the friend request
            was created.
        """

        return self.request_date

    def get_status(self):
        """
        Getter for the status of the friend request.

        Returns
        -------
        bool
            Current status of the friend request:
            - True: Friend request was accepted.
            - False: Friend request was declined.
            - None: Friend request is pending.
        """

        return self.status

    def set_sender(self, sender_instance):
        """
        Setter for the sender of the friend request.
        Does not save the change to the database.

        Parameters
        ----------
        sender_instance : Profile
            Profile instance of the target creator of the
            friend request.
        """

        self.sender = sender_instance

    def set_receiver(self, receiver_instance):
        """
        Setter for the receiver of the friend request.
        Does not save the change to the database.

        Parameters
        ----------
        receiver_instance : Profile
            Profile instance of the target receiver of the
            friend request.
        """

        self.receiver = receiver_instance

    def set_request_date(self, date):
        """
        Setter for the request date of the friend request.
        Does not save the change to the database.

        Parameters
        ----------
        date : datetime
            Target time at which the friend request was created.
        """

        self.request_date = date

    def set_status(self, state):
        """
        Setter for the status of the friend request.
        Does not save the change to the database.

        Parameters
        ----------
        state : bool
            Target state of the friend request:
            - True: Friend request was accepted.
            - False: Friend request was declined.
            - None: Friend request is pending.
        """

        self.status = state

# TODO: Models
# - Comment
# - Discussion
# - DiscussionGroup
# - Event
# - Forum
# - ForumPost
