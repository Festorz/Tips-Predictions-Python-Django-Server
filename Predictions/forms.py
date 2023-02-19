# class UserManager(BaseUserManager):
#     def create_user(self, username, first_name, last_name, email, phone, country, password):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, phone=phone, country=country, first_name=first_name,
#                           last_name=last_name)
#         user.set_password(password)
#         user.save(using=self.db)
#         return user

#     def create_superuser(self, username, email, phone, password, country=None, first_name=None, last_name=None):
#         user = self.create_user(username=username, email=email, phone=phone, password=password, country=country,
#                                 first_name=first_name, last_name=last_name)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user


# class User(PermissionsMixin, AbstractBaseUser):
#     username = models.CharField(max_length=32, unique=True, )
#     email = models.EmailField(max_length=32)
#     phone = models.CharField(max_length=13, blank=False)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     country = models.CharField(max_length=200, null=True, blank=True)

#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     REQUIRED_FIELDS = ["email", "phone"]
#     USERNAME_FIELD = "username"
#     objects = UserManager()

#     def __str__(self):
#         return self.username

  
#     class Meta:
#         ordering = ['-date_added']


# class UserManager(BaseUserManager):
#     def create_user(self, username, first_name, last_name, email, phone, country, password):
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, phone=phone, country=country, first_name=first_name,
#                           last_name=last_name)
                    
#         user.save(using=self.db)
#         return user

#     def create_superuser(self, username, email, phone, password, country=None, first_name=None, last_name=None):
#         user = self.create_user(username=username, email=email, phone=phone, password=password, country=country,
#                                 first_name=first_name, last_name=last_name)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#         return user


# class User(PermissionsMixin, AbstractBaseUser):
#     username = models.CharField(max_length=32, unique=True)
#     email = models.EmailField(max_length=255, unique=True)
#     phone = models.CharField(max_length=20, blank=False)
#     first_name = models.CharField(max_length=50, blank=True, null=True)
#     last_name = models.CharField(max_length=50, blank=True, null=True)
#     country = models.CharField(max_length=255, blank=True, null=True)
#     date_added = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     REQUIRED_FIELDS = ["email", "phone"]
#     USERNAME_FIELD = "username"

#     objects = UserManager()

#     def __str__(self):
#         return self.username

#     class Meta:
#         ordering = ['-date_added']
    

