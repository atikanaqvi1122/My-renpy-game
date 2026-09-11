# My-renpy-game
`Myrenpygame` is a short choice-driven horror visual novel made with [Ren'Py](https://www.renpy.org/). You play through a tense evening with Eileen, making decisions about a mysterious note, muddy footprints, and the locked house. Different choices lead to different endings.

## Play locally

1. Install the Ren'Py SDK from [renpy.org](https://www.renpy.org/latest.html).
2. Open the Ren'Py Launcher.
3. Add or import this repository as a project. Select the repository folder, the folder that contains `game/`.
4. Select **Myrenpygame** and click **Launch Project**.
5. Use the mouse or keyboard to advance dialogue and select choices. The **Save**, **Load**, and **Rollback** controls are available from the in-game menu.

The story starts in [`game/script.rpy`](game/script.rpy). The project uses a 1920x1080 interface and is configured for Ren'Py 8.5.3 or newer.

## Publish a playable version on GitHub Pages

GitHub Pages cannot run the `.rpy` source files directly. First create a browser build with Ren'Py's Web/HTML5 distribution, then publish the generated static files.

### 1. Build the web version

1. Open the project in the Ren'Py Launcher.
2. Choose **Build Distributions**.
3. Select the **Web** or **Web (HTML5)** distribution option.
4. Build the distribution and locate the generated web folder. It normally contains an `index.html` file plus JavaScript, WebAssembly, and game asset files.

### 2. Add the build to this repository

Copy the *contents* of the generated web folder into a directory named `docs` at the repository root. The entry point must be:

```text
docs/index.html
```

Do not upload only the `.rpy` files. The complete generated web folder is required because the browser build loads its accompanying assets and runtime files.

Commit and push the generated files:

```text
git add docs
git commit -m "Add web build for GitHub Pages"
git push
```

### 3. Enable GitHub Pages

1. Open the repository on GitHub and go to **Settings** > **Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the branch containing the build, usually `main`, and the `/docs` folder.
4. Click **Save** and wait for GitHub to publish the site.
5. Open the Pages URL shown in the same settings screen.

For a project repository, the URL is usually:

```text
https://<github-user>.github.io/<repository-name>/
```

If the game loads but cannot find assets, confirm that `docs/index.html` and all files generated beside it were committed, and that the Pages source is set to the correct branch and `/docs` folder. After rebuilding the game, replace the contents of `docs` and push the updated files.

## Project structure

```text
game/
  script.rpy   # Story, choices, and endings
  screens.rpy  # Menu and dialogue screens
  gui.rpy      # Interface configuration
  options.rpy  # Project name and build settings
```

## License

No license has been specified for this project yet.
