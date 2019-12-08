from django.contrib.sitemaps import Sitemap

class MySiteSitemap(Sitemap):
    changfreq = 'always'

    def items(self):
        return Question.objects.all()

    def lastmod(self, item):
        last_answer = Answer.objects.filter(question=item)
        if last_answer:
            return sorted(last_answer)[-1].date