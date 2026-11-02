// Point-of-sale peripherals, before factoring: IScannerAccess is a dumping ground.
using System.ServiceModel;

[ServiceContract]
public interface IScannerAccess
{
    [OperationContract] void ScanCode();
    [OperationContract] void AdjustBeam(int width, int intensity);
    [OperationContract] void OpenPort(string port, int baudRate);
    [OperationContract] void ClosePort();
}

public interface IInventoryAccess
{
    void SelectItem(string sku);
    void InsertItem(ItemData item);
    void UpdateItem(ItemData item);
    void DeleteItem(string sku);
    string GetName();
    void SetName(string name);
    int Count { get; }
}

public interface ISalesManager
{
    void Checkout(CartData cart);
    void Refund(ReceiptData receipt, string reason, int managerId, bool partial);
}

public class ItemData { public string Sku { get; set; } public string Name { get; set; } public decimal Price { get; set; } }
public class CartData { public string Id { get; set; } }
public class ReceiptData { public string Id { get; set; } public decimal Total { get; set; } public string Store { get; set; } }

public class BarcodeScanner : IScannerAccess { }
public class InventoryAccess : IInventoryAccess { }
public class SalesManager : ISalesManager, IScannerAccess { }
