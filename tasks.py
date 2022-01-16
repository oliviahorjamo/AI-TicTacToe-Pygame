from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task(coverage_report)
def view_report(ctx):
    ctx.run('firefox htmlcov/index.html')

@task
def test(ctx):
    ctx.run("pytest src")

@task
def pep(ctx):
    ctx.run('autopep8 --in-place --recursive src')
