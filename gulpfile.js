'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

// Compile's .scss into css files
gulp.task('sass', function() {
  return gulp.src('./scss/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./css'))
})

// Runs the 'sass' compile task on change of .scss files
gulp.task('sass:watch', function() {
  gulp.watch('./sass/**/*.scss', ['sass'])
})

gulp.task('default', function() {
  // TODO
});
