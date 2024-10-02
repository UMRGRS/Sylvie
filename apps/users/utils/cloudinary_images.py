from cloudinary import uploader

def upload_image(image):
    upload_data = uploader.upload(image)
    return {'secure_url': upload_data['secure_url'], 
            'public_id': upload_data['public_id']
            }

def delete_image(public_id):
    uploader.destroy(public_id, invalidate=True)

def replace_image(old_public_id, image):
    delete_image(public_id=old_public_id)
    return upload_image(image=image)
    