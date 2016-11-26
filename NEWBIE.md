# Intro

Hey, if this is your first web project, some things might be a little confusing
or scary. The Web is a terrifying place with lots more than just straight javascript.
In this project, there's a bunch of things you might not have encountered
before, so this is a no-pressure guide to dealing with the weird web tech that we use in this project. When I first
started out, I was kind of scared.

# Sass
CSS by itself has a lot that can be improved upon. Since we can't just pick
another language (CSS is the only option), one way devs fix this is by using
a language that compiles to CSS. In this case we picked [Sass](http://sass-lang.com/).

All your regular CSS works fine in Sass, as Sass is a [superset](https://en.wikipedia.org/wiki/Subset)
of CSS. The key differences between Sass and CSS are [Nesting](http://sass-lang.com/guide#topic-3)
and [Variables](http://sass-lang.com/guide#topic-2).

### Nesting
In Sass, we can take the CSS:
```
.outer { background: red; }
.outer .inner { background: blue; }
```
and rewrite it as:
```
.outer {
    background: red;
    .inner {
      background: blue;
    }
}
```

### Variables
Variables in Sass are easy ways to organize a style and
they work like you think they might.
```
$main-color = #0066BA;

button  {
  background: $main-color;
}
```

# Gulp
On the web, we often end up doing a lot of automated
tasks with our code. These can include:
- Compile [Sass](http://sass-lang.com/guide) into regular css
- [Minify](https://www.npmjs.com/package/gulp-minify) our code so it loads faster
- Run tests
- Push to production! (create a `dist`)

[Gulp](http://gulpjs.com/) is a well used library that
allows us to do a lot of these tasks.
