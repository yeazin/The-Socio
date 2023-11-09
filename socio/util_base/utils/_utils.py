"""

Socio Utility 

"""
import random
import string
import logging

logger = logging.Logger(__name__)

class SocialUtility:


    def random_code(size=12, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # Generating username
    # checking if the generated username is exists or not
    # if exists it will return a new one 
    def generate_username(instance):

        model = instance
        username_code = "socio@{}".format(SocialUtility.random_code())
        check_username = model.objects.filter(
            username=username_code
        ).only(
            "username"
        )

        if check_username.exists():
            return SocialUtility.generate_username()
        
        return username_code 
