from gqlauth.bases.mixins import RelayMixin
from gqlauth.user.resolvers import (
    ArchiveAccountMixin,
    Captcha,
    DeleteAccountMixin,
    ObtainJSONWebTokenMixin,
    PasswordChangeMixin,
    PasswordResetMixin,
    PasswordSetMixin,
    RefreshTokenMixin,
    RegisterMixin,
    RemoveSecondaryEmailMixin,
    ResendActivationEmailMixin,
    RevokeTokenMixin,
    SendPasswordResetEmailMixin,
    SendSecondaryEmailActivationMixin,
    SwapEmailsMixin,
    UpdateAccountMixin,
    VerifyAccountMixin,
    VerifySecondaryEmailMixin,
    VerifyTokenMixin,
)

__all__ = [
    "Register",
    "VerifyAccount",
    "ResendActivationEmail",
    "SendPasswordResetEmail",
    "SendSecondaryEmailActivation",
    "SwapEmails",
    "RemoveSecondaryEmail",
    "PasswordSet",
    "PasswordReset",
    "ObtainJSONWebToken",
    "ObtainJSONWebToken",
    "DeleteAccount",
    "PasswordChange",
    "UpdateAccount",
    "VerifyToken",
    "RefreshToken",
    "RevokeToken",
    "Captcha",
]


class Register(RegisterMixin, RelayMixin):
    __doc__ = RegisterMixin.__doc__


class VerifyAccount(
    VerifyAccountMixin,
    RelayMixin,
):
    __doc__ = VerifyAccountMixin.__doc__


class ResendActivationEmail(
    ResendActivationEmailMixin,
    RelayMixin,
):
    __doc__ = ResendActivationEmailMixin.__doc__


class SendPasswordResetEmail(SendPasswordResetEmailMixin, RelayMixin):
    __doc__ = SendPasswordResetEmailMixin.__doc__


class SendSecondaryEmailActivation(
    SendSecondaryEmailActivationMixin,
    RelayMixin,
):
    __doc__ = SendSecondaryEmailActivationMixin.__doc__


class VerifySecondaryEmail(VerifySecondaryEmailMixin, RelayMixin):
    __doc__ = VerifySecondaryEmailMixin.__doc__


class SwapEmails(SwapEmailsMixin, RelayMixin):
    __doc__ = SwapEmailsMixin.__doc__


class RemoveSecondaryEmail(RemoveSecondaryEmailMixin, RelayMixin):
    __doc__ = RemoveSecondaryEmailMixin.__doc__


class PasswordSet(PasswordSetMixin, RelayMixin):
    __doc__ = PasswordSetMixin.__doc__


class PasswordReset(PasswordResetMixin, RelayMixin):
    __doc__ = PasswordResetMixin.__doc__


class ObtainJSONWebToken(ObtainJSONWebTokenMixin, RelayMixin):
    __doc__ = ObtainJSONWebTokenMixin.__doc__


class ArchiveAccount(ArchiveAccountMixin, RelayMixin):
    __doc__ = ArchiveAccountMixin.__doc__


class DeleteAccount(DeleteAccountMixin, RelayMixin):
    __doc__ = DeleteAccountMixin.__doc__


class PasswordChange(PasswordChangeMixin, RelayMixin):
    __doc__ = PasswordChangeMixin.__doc__


class UpdateAccount(UpdateAccountMixin, RelayMixin):
    __doc__ = UpdateAccountMixin.__doc__


class VerifyToken(VerifyTokenMixin, RelayMixin):
    __doc__ = VerifyTokenMixin.__doc__


class RefreshToken(RefreshTokenMixin, RelayMixin):
    __doc__ = RefreshTokenMixin.__doc__


class RevokeToken(RevokeTokenMixin, RelayMixin):
    __doc__ = RevokeTokenMixin.__doc__
