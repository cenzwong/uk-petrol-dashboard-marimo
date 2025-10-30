import marimo

__generated_with = "0.17.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""# Welcome to marimo! !!! 🌊🍃""")
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(mo, slider):
    mo.plain_text(str(slider.value))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()