#import sys

def generate_template(links_path,nas_path,html_path,flag_list,main_title,short_description_path,points_to_note_path):

    """
    
    Takes the following input:
        links_path
        nas_path
        html_path
        flag_list
        main_title
        short_description
        points_to_note
    
    """
     
    # links document
    links_f = links_path
    
    # nasa ames file
    nas_f = nas_path
    
    # html base
    html_f = html_path
    
    link_list = []
    nas_list = []
    
    with open(links_f, 'r') as links:
        for line in links:
            link_list.append(line)
    
    with open(nas_f, 'r') as nas:
        for line in nas:
            nas_list.append(line)
    
    with open(html_f, 'w') as f:
    
    #generate template for the flags 
        
    
        #Use config file to show the results. 
    
        main_title_html = "<h1>" + main_title + "</h1>"
    
        points_to_note_title = "<h2><span style='font-size: 18px;'>Points to note</span></h2>"
        
        #Parse description file
        description = []
    
        with open(short_description_path, 'r') as description_f:
            for line in description_f:
                description.append(line)
    
        #Parse points to note file
        points_to_note = []
    
        with open(points_to_note_path, 'r') as points_f:
            for line in points_f:
                points_to_note.append(line)    
        
        flag_title_html = "<h2><span style='font-size: 18px;'>Flags commonly used with this format:</span></h2>"
        flags_html = "<code data-gist-id='5d878cfa3a95ea872259ddc3c945fb19' data-gist-line='" + flag_list  + "' data-gist-hide-line-numbers='true' data-gist-hide-footer='true' data-gist-highlight-line='1,3,5'></code>"
        template_title_html = "<h2><span style='font-size: 18px;'>Template for Data Submission:</span></h2>"
    
        # gist-embed
        f.write("<head>")
        f.write("<script type='text/javascript' src='https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js'></script>")
        f.write("<script type='text/javascript' src='http://folk.nilu.no/~richard/gist-embed.js'></script>")
        f.write("</head>")
        
        #body content of template     
        
        f.write("<div id='template-container' style='font-family:arial;'>")
    
        f.write(main_title_html) 
    
        for content in description:
            f.write("<p>" + content  + "</p>")
    
        f.write(points_to_note_title)
    
        #Start creating list
        f.write("<ul>")
        
        for bullet_point in points_to_note:
            f.write("<li>" + bullet_point +  "</li>")
        
        f.write("</ul>")
            
        f.write(flag_title_html)
        f.write(flags_html)
        f.write(template_title_html)
        
        i = 0
        for line in nas_list:
            if ':' in line:
    
                split = line.split(':')
    
                count = 40 - len(split[0])
    
                nbsp = "&nbsp;" * count
    
                f.write("<a style='font-family:courier,monospace;text-decoration:none;' href='" + link_list[i].strip() + "'>" + split[0] + ":" + nbsp + split[1].replace(" ", "") + "</a>" + "<br>")
            else:
                f.write("<a style='font-family:courier,monospace;text-decoration:none;' href='" + link_list[i].strip() + "'>" + line.strip() + "</a>" + "<br>")
            i += 1
    
        f.write("</div>")
    
    
        
    print("You generated template successfully, and can find it here: ", html_path)
