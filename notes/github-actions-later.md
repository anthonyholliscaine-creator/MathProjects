# GitHub Actions Later

This note is here for future you.

Right now, this website is simple:

- it is just HTML, CSS, JavaScript, Python files, and MP4 files
- GitHub Pages can host those files directly from the `main` branch
- there is no build step
- there is nothing to "compile" before publishing

That is why we are **not** using GitHub Actions right now.

## Why Keeping It Simple Makes Sense

For this project, the simple version is easier to understand:

- you edit files
- you push them to GitHub
- GitHub Pages shows those files on the web

That means fewer moving parts and fewer things to troubleshoot.

## What GitHub Actions Is

GitHub Actions is an automation system inside GitHub.

You can think of it as:

"When something happens in the repository, automatically run a sequence of steps."

For example:

- when you push code, automatically publish the site
- when you upload files, automatically process them
- when you change content, automatically build a cleaner final website

## When You Might Want It Later

You might consider GitHub Actions later if this site becomes more complicated.

Some examples:

### 1. You Want a Build Step

Right now the site is plain files.

Later, you might use a tool that:

- combines templates into pages
- generates navigation automatically
- converts markdown into HTML
- creates a more polished site from source files

If that happens, GitHub Actions can build the site for you before publishing it.

### 2. You Want to Publish Only a Clean Output Folder

Sometimes people do not want GitHub Pages to serve the whole repository directly.

Instead, they want:

- source files in one place
- final website files in another place

GitHub Actions can generate that final output automatically.

### 3. You Want Automatic Checks

You might later want GitHub to check things before publishing, such as:

- whether links are broken
- whether files are missing
- whether pages still load correctly

Actions can run those checks automatically.

### 4. You Want to Process Media Automatically

Later, you might want GitHub to help with repetitive tasks like:

- resizing images
- optimizing files
- generating thumbnails
- copying content into the right folders

Actions can do that kind of repetitive work.

### 5. You Want More Structured Publishing

If the site grows into many simulations, course notes, and videos, you may want a more formal publishing pipeline.

That is the kind of moment when Actions starts becoming useful.

## When You Probably Do Not Need It

You probably do **not** need GitHub Actions if:

- you are editing a few static pages by hand
- you are uploading a few MP4 files
- you are adding Python files and links manually
- GitHub Pages is already showing the site correctly

That is your current situation.

## Simple Rule of Thumb

Use the simple branch-based GitHub Pages setup as long as:

- the site is easy to update by hand
- publishing feels straightforward
- you are not repeating annoying setup work over and over

Consider GitHub Actions only when you start thinking:

"I keep doing the same technical steps every time. I wish GitHub would just do this for me."

## Bottom Line

Right now:

- simple GitHub Pages from `main` is the right choice

Later:

- GitHub Actions may be worth it if the site needs automation, processing, validation, or a build step

For now, you are not missing anything important by skipping Actions.
