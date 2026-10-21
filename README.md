# Myrenpygame

ok so this is my first ever try at making a visual novel lol. it's a short horror one made with Ren'Py. you play as someone spending a creepy evening with Eileen and you pick what to do about a weird note, some muddy footprints, and a locked house. depending on what you pick you get different endings (some are kinda cooked)

heads up i had no idea how to make characters so i made them with AI. same for some of the other stuff in here. i'm still learning so don't expect anything crazy

to play it on your pc:
download Ren'Py from renpy.org, open the launcher, and add this repo folder as a project (the folder that has game/ inside it). then pick Myrenpygame and hit Launch Project. click or use keyboard to move the dialogue and choose stuff. save, load and rollback are in the in-game menu so you can go back and try the other endings

the story starts in game/script.rpy if you wanna look at it. it's 1920x1080 and needs Ren'Py 8.5.3 or newer

if you wanna put it online on github pages:
github pages can't run the .rpy files directly so you have to make a web build first. in the Ren'Py launcher click Build Distributions and pick the Web option. when it's done copy everything inside the web folder into a folder called docs in the repo (so you end up with docs/index.html). dont just upload the .rpy files it wont work, you need everything the build makes. then git add docs, git commit, git push

then on github go to Settings > Pages, pick deploy from a branch, choose main and the /docs folder, save, and wait a bit. your link will be something like https://your-username.github.io/repo-name/

if the game loads but stuff is missing, check that all the files in docs got pushed and that pages is set to main + /docs. if you rebuild the game just replace whats inside docs and push again

files:
game/script.rpy is the story, choices and endings
game/screens.rpy is menus and dialogue screens
game/gui.rpy is the interface stuff
game/options.rpy is the project name and build settings

Thank you for reading
