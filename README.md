# Bell Senior Society Website

### Startup Guide

To start developing locally we need to run the following commands. First, initialize and download the `LoveIt` submodule that we use at the theme for this Hugo site:
```
> git submodule init  
Submodule 'themes/LoveIt' (https://github.com/dillonzq/LoveIt.git) registered for path 'themes/LoveIt'
> git submodule update
Cloning into '/Users/campbellphalen/Desktop/bell-website/themes/LoveIt'...
Submodule path 'themes/LoveIt': checked out 'eaddd23bda7c77c07907e590ea7c5415f9abfc47'
```
Once you have the theme installed, you can run the site in development mode with Hugo:
```
> hugo serve -D
```
Hugo will hot-reload changes you make to the site, so no need to restart the process as you make changes (just reload the page).

If you do not already have Hugo installed, you can find installation instructions [here](https://gohugo.io/getting-started/installing/). On macOS, you can just run `brew install hugo`.


### Contributors

Right now we've got Ben Demers, Campbell Phalen, Danny Bessinov, and Praneeth Alla working on the site. Reach out to us if you want to contribute!