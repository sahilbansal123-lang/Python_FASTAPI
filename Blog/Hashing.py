from passlib.context import CryptContext

## encryption
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    @staticmethod
    def verify(hashed_Password, Plain_password):
        return pwd_cxt.verify(Plain_password, hashed_Password)