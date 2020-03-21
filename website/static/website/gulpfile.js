var gulp = require('gulp');
var sass = require("gulp-sass");
var del = require('del');

gulp.task('styles', () => {
  return gulp.src('./styles/scss/custom.scss')
    .pipe(sass({includePaths: ['node_modules']}).on('error', sass.logError))
    .pipe(gulp.dest('./styles/'))
});

gulp.task('clean', () => {
  return del([
    './styles/custom.css'
  ]);
});

gulp.task('default', () => {
  gulp.watch('./styles/scss/*.scss', gulp.series(['clean', 'styles']))
});
