def remove_url_anchor(url):
    return url.split('#')[0]

print(remove_url_anchor('www.codewars.com#about'))
print(remove_url_anchor('www.codewars.com?about'))