import nox
import tempfile

package = "feinstaub-api"
nox.options.sessions = "black", "lint", "safety"
locations = "noxfile.py", "feinstaub"


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    install(session, "black")
    session.run("black", *args)


@nox.session(python="3.8")
def lint(session):
    args = session.posargs or locations
    install(
        session,
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python="3.8")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


def install(session, *args, **kwargs):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


# TODO: Coverage
# TODO: Doc
# TODO: Tests
# TODO: Type hints maybe. What do you think @ahoneiser?
