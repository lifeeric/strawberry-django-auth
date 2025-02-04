from gqlauth.bases.mixins import ArgMixin
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


class Register(RegisterMixin, ArgMixin):
    __doc__ = RegisterMixin.__doc__


class VerifyAccount(
    VerifyAccountMixin,
    ArgMixin,
):
    __doc__ = VerifyAccountMixin.__doc__


class ResendActivationEmail(
    ResendActivationEmailMixin,
    ArgMixin,
):
    __doc__ = ResendActivationEmailMixin.__doc__


class SendPasswordResetEmail(SendPasswordResetEmailMixin, ArgMixin):
    __doc__ = SendPasswordResetEmailMixin.__doc__


class SendSecondaryEmailActivation(
    SendSecondaryEmailActivationMixin,
    ArgMixin,
):
    __doc__ = SendSecondaryEmailActivationMixin.__doc__


class VerifySecondaryEmail(VerifySecondaryEmailMixin, ArgMixin):
    __doc__ = VerifySecondaryEmailMixin.__doc__


class SwapEmails(SwapEmailsMixin, ArgMixin):
    __doc__ = SwapEmailsMixin.__doc__


class RemoveSecondaryEmail(RemoveSecondaryEmailMixin, ArgMixin):
    __doc__ = RemoveSecondaryEmailMixin.__doc__


class PasswordSet(PasswordSetMixin, ArgMixin):
    __doc__ = PasswordSetMixin.__doc__


class PasswordReset(PasswordResetMixin, ArgMixin):
    __doc__ = PasswordResetMixin.__doc__


class ObtainJSONWebToken(ObtainJSONWebTokenMixin, ArgMixin):
    __doc__ = ObtainJSONWebTokenMixin.__doc__


class ArchiveAccount(
    ArchiveAccountMixin,
    ArgMixin,
):
    __doc__ = ArchiveAccountMixin.__doc__


class DeleteAccount(DeleteAccountMixin, ArgMixin):
    __doc__ = DeleteAccountMixin.__doc__


class PasswordChange(PasswordChangeMixin, ArgMixin):
    __doc__ = PasswordChangeMixin.__doc__


class UpdateAccount(UpdateAccountMixin, ArgMixin):
    __doc__ = UpdateAccountMixin.__doc__


class VerifyToken(VerifyTokenMixin, ArgMixin):
    __doc__ = VerifyTokenMixin.__doc__


class RefreshToken(RefreshTokenMixin, ArgMixin):
    __doc__ = RefreshTokenMixin.__doc__


class RevokeToken(
    RevokeTokenMixin,
    ArgMixin,
):
    __doc__ = RevokeTokenMixin.__doc__
