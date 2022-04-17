using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OnClickPickup : MonoBehaviour
{
    public GameObject GunInDrawer;
    public GameObject GunInHand;
    public GameObject aCamera;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
   /*     RaycastHit hit;
        Physics.Raycast(aCamera.transform.position, aCamera.transform.forward, out hit);
        if (hit.transform.gameObject == GunInDrawer.gameObject && hit.distance < 5)
        {
            
            if (Input.GetKeyDown(KeyCode.F))
            {
                GunInDrawer.SetActive(false);
                GunInHand.SetActive(true);
            }
        }
        */
    }
    
  
    
    
    private void OnMouseDown()
    {
        GunInDrawer.SetActive(false);
        GunInHand.SetActive(true);
    }
}
