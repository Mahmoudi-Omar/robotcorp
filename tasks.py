from robocorp.tasks import task
from robocorp import browser,http,excel
from RPA.Tables import Tables

@task
def order_robots_from_RobotSpareBin():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    open_robot_order_website()
    orders = get_orders()
    for order in orders : 
        fill_order_form(order)

def open_robot_order_website() :
    # TODO: Implement your function here
        http.download(url="https://robotsparebinindustries.com/orders.csv", overwrite=True)

def get_orders() :
     library = Tables()
     orders = library.read_table_from_csv("orders.csv", columns=["Order", "number", "Head","Body","Legs","Address"])
     return orders

def fill_order_form () :
     