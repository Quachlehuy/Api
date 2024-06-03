from flask import Flask, request, jsonify
import asyncio
import re
from aiohttp import ClientSession
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def huy():
    return '<h1>Huyy Api</h1>'

@app.route('/api/flu')
def fluxus():
    link = request.args.get('url')
    if link:
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'close',
            'Referer': 'https://linkvertise.com'
        }

        urls = [
            link ,
            'https://flux.li/android/external/check1.php',
            'https://flux.li/android/external/main.php'
        ]

        key_regex = r'let content = \("([^"]+)"\);'


        async def get_content(url, session):
            async with session.get(url, headers=headers, allow_redirects=True) as response:
                return await response.text()

        async def main():
            async with ClientSession() as session:
                responses = []
                for url in urls:
                    responses.append(await get_content(url, session))
                soup = BeautifulSoup(responses[-1], 'html.parser')
                k = soup.find('script', type="text/javascript")
                key_match = re.search(key_regex, str(k))
                if key_match:
                    key = key_match.group(1)
                    return {'Key': key}     
                else:
                    return {'error': 'Key not found'}
                    
        return asyncio.run(main())
    else:
        return {'error': 'Link not found'}

if __name__ == '__main__':
    app.run(debug=True)
