# Iterate over the objects in the bucket
for obj in response.get('Contents', []):
    # Get the object key
    object_key = obj.get("Key")

    if object_key:
        # Create the full file path using the file location
        file_path = os.path.join(file_location, object_key)

        # Call Amazon Textract to start document analysis job for the object
        try:
            response = textract.start_document_text_detection(
                DocumentLocation={
                    'S3Object': {
                        'Bucket': s3BucketName,
                        'Name': object_key
                    }
                }
            )

            # Get the JobId for the document analysis job
            job_id = response['JobId']

            # Poll for the completion of the document analysis job
            while True:
                response = textract.get_document_text_detection(JobId=job_id)

                status = response['JobStatus']
                if status in ['SUCCEEDED', 'FAILED']:
                    break

                time.sleep(5)  # Wait for 5 seconds before polling again

            if status == 'SUCCEEDED':
                # Get the results of the document analysis job
                blocks = response['Blocks']

                # Extract text from each block
                text = ''
                for block in blocks:
                    if block['BlockType'] == 'LINE':
                        text += block['Text'] + '\n'

                # Summarize the text into 3 sentences
                summary = summarize(text, ratio=0.2, split=True)
                summary_text = ' '.join(summary[:3])

                # Append the file title, original text, and summary to the data list
                data.append({'File Title': object_key, 'Text': text, 'Summary': summary_text})

                print(f"Text extracted for {object_key}")
            else:
                print(f"Error processing {object_key}: Document analysis job failed")
        except Exception as e:
            print(f"Error processing {object_key}: {str(e)}")
    else:
        print("Object key is None")
