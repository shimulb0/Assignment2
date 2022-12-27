def h2(text):
    """
    This function converts from normal text to WordPress Gutenberg h2
    """
    code_h2 = f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'
    return code_h2

def h3(text):
    """
    This function converts from normal text to WordPress Gutenberg h3
    """
    code_h3 = f'<!-- wp:heading {{"level":3}} --><h3>{text}</h3><!-- /wp:heading -->'
    return code_h3

def h4(text):
    """
    This function converts from normal text to WordPress Gutenberg h4
    """
    code_h4 = f'<!-- wp:heading {{"level":4}} --><h4>{text}</h4><!-- /wp:heading -->'
    return code_h4

def h5(text):
    """
    This function converts from normal text to WordPress Gutenberg h5
    """
    code_h5 = f'<!-- wp:heading {{"level":5}} --><h5>{text}</h5><!-- /wp:heading -->'
    return code_h5

def h6(text):
    """
    This function converts from normal text to WordPress Gutenberg h6
    """
    code_h6 = f'<!-- wp:heading {{"level":6}} --><h6>{text}</h6><!-- /wp:heading -->'
    return code_h6

def paragraph(text):
    """
    ***** This function converts from normal text to WordPress Gutenberg Paragraph *****
    """
    codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return codes

def media(image_url, name):
    """
    ---------------------------------------------------------------------------------
    This function converts from normal Image Url to WordPress Gutenberg Image Formate
    *********************************************************************************
    ---------------------------------------------------------------------------------
    Input Image url : image_url
    ----------------------------------------------------------------------------------
    Input Image Alt Text : alt_text
    ----------------------------------------------------------------------------------
    Input Caption : caption
    ----------------------------------------------------------------------------------
    """

    codes = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} -->' \
            f'<figure class="wp-block-image aligncenter size-large is-resized">' \
            f'<img src="{image_url}" alt="{name}"/>' \
            f'<figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    return codes


def wp_code(text):
    """
    This function converts from normal code to WordPress Gutenberg code
    """

    codes = f'<!-- wp:code --><pre class="wp-block-code"><code>{text}</code></pre><!-- /wp:code -->'
    return codes

def wp_youtube(url, caption):
    """
    This function converts from normal Youtube Url to WordPress Gutenberg embed Youtube Url
    """
    codes = f'<!-- wp:embed {{"url":"{url}","type":"video","providerNameSlug":"youtube","responsive":true,' \
            f'"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"}} ' \
            f'--><figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-' \
            f'16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">{url}' \
            f'</div><figcaption class="wp-element-caption">{caption}</figcaption></figure><!-- /wp:embed -->'
    return codes

def list_item(text):
    '''
    -------------------------------------------------------------------------------
    This function converts from normal Python list text to WordPress Gutenberg list
    :param text: Input Always item *** example : ['Bangladesh','India'] ***
    :return: WordPress Gutenberg list
    -------------------------------------------------------------------------------
    '''
    starts = '<!-- wp:list --><ul>'
    for e in text:
        starts += f'<!-- wp:list-item --><li>{e}</li><!-- /wp:list-item -->'
    end = '</ul><!-- /wp:list -->'
    codes = starts+end
    return codes

def wp_tabel(dictionary):
    '''
    This function converts from dictionary text key to WordPress Gutenberg table
    ------------------------------------------------------------------------
    param :dictionary text key
    return: Gutenberg table
    '''
    codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dictionary.items():
        tr_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        codes += tr_data
    codes += '</tbody></table></figure><!-- /wp:table -->'
    return codes