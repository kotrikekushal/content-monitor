from .models import Keyword, ContentItem, Flag

def scan_content_logic():

    keywords = Keyword.objects.all()
    contents = ContentItem.objects.all()

    for keyword in keywords:
        keyword_lower = keyword.name.lower()

        for content in contents:
            title = content.title.lower()
            body = content.body.lower()

            title_words = title.split()
            body_words = body.split()

            score = 0

            if keyword_lower in title_words:
                score = 100

            elif keyword_lower in title:
                score = 70

            elif keyword_lower in body_words:
                score = 40

            if score > 0:

                existing_flag = Flag.objects.filter(
                    keyword=keyword,
                    content_item=content
                ).first()

                if existing_flag:

                  
                    if existing_flag.status == 'irrelevant':
                        if content.last_updated <= existing_flag.last_reviewed_at:
                            continue

                    existing_flag.score = score
                    existing_flag.status = 'pending'
                    existing_flag.save()

                else:
                    Flag.objects.create(
                        keyword=keyword,
                        content_item=content,
                        score=score,
                        status='pending'
                    )