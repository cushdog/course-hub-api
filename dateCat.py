import requests
from bs4 import BeautifulSoup
import re
import json

def extract_wrapped_json(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', string=re.compile('indexPageData'))
    
    if not script_tag:
        return None
    
    return script_tag.text

def retrieve_events():

    # URL to send the GET request to
    url = "https://apps.atlas.illinois.edu/datecat/Student"

    # Headers that were sent with the original request
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "dnt": "1",
        "referer": "https://apps.atlas.illinois.edu/datecat/Home/Beta",
        "sec-ch-ua": '"Not;A=Brand";v="24", "Chromium";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }

    # Cookies that were sent with the original request
    cookies = {
        "datecatweb": "CfDJ8Ow6Ynt4V2dOmWf4jt9x5EcSGbbdUH-ujRb3iTQcPaoZQ8ROTY01CIr-lKvD_q3X07KcHO1aZRXAdWPgzG3xWcFyP26lVbWAzYAxzg8tCXUvfB5SeQWWCDlpqqleVKb6cCyS2qfH2O0f_wkrNifzZDHM2DfRpqsHqZa42HyBxxCmDOTGC7-BYQTL0nw8ObZke6jFAhGPEW4hQhKIustuXPRT2dERhHiwnjUlDr3rcdb6IjsTc2vRA6Wy7YWkYiJ-vixqT26TiufEpmyuA6Wox1QtKvxqBLS5R0ewijfr1gdtBhPxGVV27d7mFXRuamJIkrduvaLPmBUSu7y0GeJfMnCj5GWhpYWlSf9FK_LRPlRhOW8TznXzzZuewErtEZ4_O0jABGs2s71PsMDQnwmJmQjVvdsAj7cXCt_ptG8olvU0xT01LS6g8tWBink3ns0gEGKW8RJcrIneeDH1ch1bdsLdX3TmxyukSiCQxReF_v0NNpbJUMDwtSBTwK0efl2qWikCQGx2M2rMpQfr1c8AYnUh5aG6BWATREitCZPTIaDQ1xH3uj3v-duA7ijgUMbvEAWToQSlQFe4xOhRlxvh4fZuzl08-KvAFJ1fTCU4JdUAYBQh613vWReXMOYH2JLz1PELw7wU5_A_o844tKhnuk7y0ssOD-7LFGi381EUiTkfYcWNiK9iSRW16vjK9ENxDlPEqoCTh8W7_A5lK-FRkexPTx9_mc-fRlr69w0NWz8oQyzYHKwG_-8YCzobaJQEB7xseZG-uc5lEePNx5I8mI-tY1yLhKgmwPPK1gwG5rpvsXqepavMcDC6EkAB-M4oyT40wJ_wCBUMJzdu76btLwvfrP-hPOad6FS5SFi7mZfLwpQF8jS_ZiEH9soO-rEICLS5qgEgtDXiW6oykP_FNJ0vS8iE-D6CHhX6sIMfs9Z-85RCwhPDas7u1EgLPHxJqOGXthV6q8jXplH0M-_i_32QY-48zvyBhVO7JCaxHxS56bz2Sf5m3_CDRBSoNl8Br3maY0xrYTX8q3x9_Z8NG8pUb8ziF5O4fR2Fgk2WsSao3FppWjfVPacOuDrl8Mixh0GGWRRrsLKAPmv0Y-bFGH-JBDyJRNNZBSyjd1bvTXkg5hrKiRIUDZEAhnBotIJroTJ5p1K59psBcInYTyNw-y3IPfCudzWYfN5wU0mnqAAgBP7zblJnyZpA5jTo9W4fti3fvEe7UzIdua9QC0BZRe-lapJvG63RMwD_uivD8fdZqrgRrREKHXtRJiFUV9mTMDipL3s8k05iUN2s8oXQMQwdL6qlXsS5gjpSRE3-UciiBv92rqrrRrJuu8cnogwitt0MiMBB2YJxIkxWGtzYbb8d7vb6oxtdXY9g2cBJZYzOb_rqY3v6ZT4OBQUU5N7aOgYETgZrAnoRZ9ffRnJPFs0RC_VVUJwku_UeQsjMbrrOmaRoYUVNZ-1MJVFeOxJSvsJv7yn6f4zY_ZyGEH2S-2xU2Ewwqj0r1fsoRiqM8z1cznmlTNtoTbYyPfKPeaMr-hdU9L5sh6o_XnF_aHnxeWT0KWqQTxCFSS7FprhkrJPYxKaiJdAL-V4Ebyeh-WjEeRh0_2zqbGKC1TlVjX-7qRjOXoPvshzOByOrlFn3EXrqnY5TisU6hQZ1uCbn-LpWS5S-HqBM9mINOa3WpPKKWpuCTyqrXXrLgE4-QNSuHZKwuV_jNA9n0JmYzLBHjSztzW1MQT230hNujhPleSq7b7E8qhkNLAL6e7UQg3b82gd_MT6Hl3VlaHhvovYTiQP-hn7yJ7FTWn0Wl6h1BoW-C508_SgZDQktv5jnx-y9AJE1PZKdg7ycOaoYP9LuFWUBxKhVGHaWrzZrgUehE7Jm4kJYZNrTYCV9IgmOUWdEPKE2XQwafYU9RD22F-VXcd7O8gfUAYxbz0AyJQC7nJyAtyReZ11RC-DDfiEiCKY9HEz_d0pFY9p_985J5VioXnhYGtbkPd7jsL3dF7axhuNaovW6mTNuQiOUVzd3bNOnDFJ5BY-845zUdUGerpldPAny2zGkdjKWSh6F2Whe_k-sWVn3ph9N0UK4eCNfoV48yWH8Uw05yeLgSyYh6NRpUvMS9l0nbdsNF5_MymEP98MEEodvJtzXiUbWgXcOL9El3hpqXoi-5R0Dws8Vx4-B_tFQOMTB7UckNp_H3ZI81iR8ldb5DNB2XSfMqCaShivC7B1MpQXKFfweityEpjLLyLstUAaVVxRYJ42tobohIGp0gR3T9DL_NKx4SPG_gQwt4bfEDvXK8ptv5LxGjvMARsJq-e5qO64WA4A5osvG2WFtG9cCpzhhUR1M06Uyzc4zP9-HsUTyo4omJL0TP8j-5J0LTEANpoDXzc4u7hWogl9_jGA5gRduWb8CNicIY8QMu1Qut1ryzA4JX0Rl7m-dr6zLXVJLefXPd_w81mFN3ZkR0oOEwCLWSdnPX0uLtavzKKVTYgVL8VwUYU-WqTxlZLC12s_4CnUq2FKuaOUpSa9aCort0VEsSmFD5UxihB6skMB-Vy6xTVcGA3Y-CLBYStU90Dwdd0tHu-KWAbjeXRv3e5xGqF26zTey1KJOXcosMGkxwWy7IxWmPae01JB3GWGGhrBdVBEcgseJYhHlVICpEaDBwCL3tMdeXeNmuc9o5JstAxpSNvwJQkO3Hvp2VilpdzOxtmJxBDwEUjkFHiFNH5K16KtWbMBddbEZmdgkkYQQZcnRhUL3HTatBLqQLqC7inlpfwYwMZv0_L5CvSy1pq2DyJpev0Ctni6TNqlDMAmdYcQY4Y8AlU_8H-qDzBxyJ2zZDRLHIarJ3TBxha2traOqVZEN_rOJiFv6Mo9OW25zQOCsEmUvgxjGX3jmwifYVA"
    }

    # Send the GET request
    response = requests.get(url, headers=headers, cookies=cookies)

    text = extract_wrapped_json(response.content)

    # The string to search for at the beginning
    start_search_string = "(w['indexPageData']="

    # Finding the position of the start string
    start_position = text.find(start_search_string)

    # Extracting everything after the start string
    if start_position != -1:
        result = text[start_position + len(start_search_string):]
    else:
        result = None  # Handle the case where the string is not found

    # The string to search for at the end
    end_search_string = ',"feeds":{"newFeedIds"'

    # Finding the position of the end string within the result
    end_position = result.find(end_search_string)

    # Trimming everything after the end string
    if end_position != -1:
        result = result[:end_position]
    result += "}"  # Add a closing curly brace

    # Write result to a file
    # with open('test.json', 'w') as f:
    #     f.write(result)


    # Step 7: Clean and parse the JSON-like data
    events_data = json.loads(result)

    # Step 8: Pretty print the JSON data
    pretty_json = json.dumps(events_data, indent=4)
    print(pretty_json)
    return pretty_json