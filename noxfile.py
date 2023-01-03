import nox
from nox import Session


@nox.session
def test(session: Session):
    session.run("poetry", "install", external=True)
    session.run("pytest")
