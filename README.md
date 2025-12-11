# Scikit-image tutorials

Adapted from:

* https://lectures.scientific-python.org/advanced/image_processing/index.html#opening-and-writing-to-image-files
* https://lectures.scientific-python.org/packages/scikit-image/index.html

## To do

> Looks good in general.

> However, I missed a good explanation of why replacing the pixel value with
its corresponding position in the CDF gives a uniform distribution. Did you
run across a good explanation somewhere?

> Can you add that?

- Show 3D edge detection kernels, it is visually obvious how they detect gradients
which correspond to edges.

- Maybe show the between classes variances for the Otsu method (show that it converges on same threshold?)...

- Notes for potential additions to Gaussian filtering section: Use gaussian from here: https://sbme-tutorials.github.io/2018/cv/notes/4_week4.html [Highlight that skimage filter is built from NumPy and SciPy - wrapper for `scipy.ndimage.gaussian_filter`?]

## Notes and admonitions

Use `:::` for
`<div>` blocks ([JupyterBook allows
this](https://jupyterbook.org/en/stable/content/content-blocks.html#markdown-friendly-directives-with)):
So, for example, prefer:

~~~
::: {note}

My note

:::
~~~

to the more standard Myst markup of:

~~~
<!-- #region -->
``` {note}

My note

```
<!-- #endregion -->
~~~

Note the `region` and `endregion` markup in the second form; this makes more
sure that Jupytext does not confuse the `{note}` with a code block.  One of the
advantages of the `:::` markup is that you don't need these `#region`
demarcations.

For the same reason, prefer the `:::` form for other content blocks, such as
warnings and admonitions.  For example, prefer:

~~~
::: {admonition} A custom title

My admonition

:::
~~~


## Exercises and solutions

We use [sphinx-exercise](https://ebp-sphinx-exercise.readthedocs.io) for the exercises and solutions.

Mark *all* exercises and solutions with [gated
markers](https://ebp-sphinx-exercise.readthedocs.io/en/latest/syntax.html#alternative-gated-syntax),
like this:

~~~
::: {exercise-start}
:label: my-exercise-label
:class: dropdown
:::

My exercise.

::: {exercise-end}
:::

::: {solution-start} my-exercise-label
:class: dropdown
:::

My solution.

::: {solution-end}
:::
~~~

The gated markers (of form `solution-start` and `solution-end` etc) allow you
to embed code cells in the exercise or solution, because this allows code cells
to be at the top level of the notebook, where Jupyter needs them to be.

The gated markers also make it possible for the `process_notebooks.py`
script to recognize exercise and solutions blocks, to parse them correctly.

## Development

Run this once, in the repository directory:

```
pip install pre_commit
pre-commit install
```

Before each commit that you will push:

```
pre-commit run --all
```

Among other things, this runs the `codespell` check, also run by CI.
