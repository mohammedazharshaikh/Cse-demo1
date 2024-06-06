# from flask import Flask, render_template
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def gallery():
    

#     try:
#         data = pd.read_csv('src/people.csv')
#         print(data.head())
#         data['Salary'] = data['Salary'].str.strip().replace('', np.nan).fillna(0)

#         data['Salary'] = data['Salary'].astype(int)  # Convert salary to int
#         print(data['Salary'].dtype) 
#         filtered_data = data[data['Salary'] < 99000]
#         print(filtered_data)
#         images = [f"/static/images/{row['filename']}" for index, row in filtered_data.iterrows()]
#         return render_template('gallery.html', images=images)
#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)

# -----------------------

# from flask import Flask, render_template
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def gallery():
#     try:
#         data = pd.read_csv('src/people.csv')
#         print("Data loaded successfully:", data.head())  # Display the first few rows of the CSV

#         data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce').fillna(0)
#         print("Salaries after conversion:", data['Salary'])  # Check salary conversion

#         filtered_data = data[data['Salary'] < 99000]
#         print("Filtered data:", filtered_data)  # Display filtered data

#         images = [f"/static/images/{row['filename']}" for index, row in filtered_data.iterrows()]
#         print("Image URLs:", images)  # Check the final list of image URLs

#     except Exception as e:
#         images = []
#         print(f"Error: {e}")

#     return render_template('gallery.html', images=images)

# if __name__ == '__main__':
#     app.run(debug=True)
# ---


# import os
# from flask import Flask, render_template
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def gallery():
#     try:
#         data = pd.read_csv('src/people.csv')
#         data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce').fillna(0)
#         filtered_data = data[data['Salary'] < 99000]

#         images = [f"/static/images/{row['filename'].strip()}" for index, row in filtered_data.iterrows()]
        
#         # Debugging: Check if the image files actually exist
#         for img in images:
#             print(img, os.path.exists(f"static/{img}"))  # Note: Adjust the path according to your app structure

#     except Exception as e:
#         images = []
#         print(f"Error: {e}")

#     return render_template('gallery.html', images=images)

# if __name__ == '__main__':
#     app.run(debug=True)
# ----

# import os
# from flask import Flask, render_template
# import pandas as pd

# app = Flask(__name__)

# @app.route('/')
# def gallery():
#     images = []
#     try:
#         data = pd.read_csv('src/people.csv')
#         data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce').fillna(0)
#         filtered_data = data[data['Salary'] < 99000]
#         print(filtered_data)

#         for index, row in filtered_data.iterrows():
#             image_path = f"static/images/{row['Picture']}"
#             print(image_path)
#             if os.path.exists(image_path):
#                 images.append(f"/{image_path}")
#                 print(image_path)
#             else:
#                 print(f"File not found: {image_path}")  # This will show in the console

#     except Exception as e:
#         print(f"Error: {e}")

#     return render_template('gallery.html', images=images)

# if __name__ == '__main__':
#     app.run(debug=True)
# -

import os
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def gallery():
    images = []
    try:
        data = pd.read_csv('src/people.csv')
        data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce').fillna(0)
        filtered_data = data[data['Salary'] < 99000]
        
        for index, row in filtered_data.iterrows():
            image_path = f"static/images/{row['Picture']}"
            if os.path.exists(os.path.join(app.static_folder, "images", row['Picture'])):
                images.append(f"/{image_path}")
            else:
                print(f"File not found: {os.path.join(app.static_folder, 'images', row['Picture'])}")

    except Exception as e:
        print(f"Error: {e}")

    return render_template('gallery.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)

