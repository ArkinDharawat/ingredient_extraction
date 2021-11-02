## Setup Doccano
We will use [Doccano](https://github.com/doccano/doccano) to annotate the data. 

###Docker command for setup
```shell script
docker pull doccano/doccano
docker container create --name ner_test \
  -e "ADMIN_USERNAME=admin" \
  -e "ADMIN_EMAIL=admin@example.com" \
  -e "ADMIN_PASSWORD=password" \
  -p 8000:8000 doccano/doccano
```
You'll only 
have to do this step once since we will mainly import/export the dataset from the server.

### Start and run the server
- Starts the server
    ```shell script
    docker container start doccano
    ```
- Go to `http://0.0.0.0:8000/` and you'll see the front page of the server. Login using the admin
credentials.
- Once logged in, setup a project and make sure to select `sequence to sequence labelling`, the interface will be 
different if you select something else. 
- Upload the txt file or jsonl file as a the `dataset` and click `injest` this should upload the dataset for labelling.

### Annotation and downloading.
- Annotation should be pretty straight forward after you select the `dataset` tab.
- Once you're done export the datasets. You'll get a zip folder which contains 2 `.jsonl` files: `admin.jsonl` and `unknown.jsonl`.
- To stop the container just run
    ```shell script
    docker container stop doccano
    ```
- The next time you start annotation make sure to upload the `unknown.jsonl` to the dataset since thi 
contains the un-annotated data. 
- You can merge the files by running `cat a.jsonl b.jsonl ... > merged.jsonl`. This should ideally be done once you have 
annotated all the files. 
