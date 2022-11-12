SELECT owner_id AS 'owner ID', 
owner_name AS 'owner Name', 
different_category_count, COUNT(1) AS 'number of different categories of the articles the owner owns',
FROM '.category_article_mapping' AS db
INNER JOIN '.category_article_mapping.article.owner' AS ao
ON '.category_article_mapping.category'
GROUP BY owner_name
ORDER BY different_category_count DESC
