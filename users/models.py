from django_mongoengine import fields, Document
import bcrypt


class User(Document):
    SUBSCRIPTION_TYPES = ["free", "basic", "premium", "vip"]

    email = fields.EmailField(unique=True, required=True)
    # username = fields.UserNameField(unique=True, required=True)

    first_name = fields.StringField(required=True)
    last_name = fields.StringField(required=True)
    password_hash = fields.StringField(required=True)
    has_subscription = fields.BooleanField(default=False)
    subscription_type = fields.StringField(default="free", choices=SUBSCRIPTION_TYPES)
    subscription_expiry = fields.DateTimeField()

    # 👇 REQUIRED for compatibility with django_mongoengine.mongo_auth
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(
            password.encode("utf-8"),
            self.password_hash.encode("utf-8")
        )
