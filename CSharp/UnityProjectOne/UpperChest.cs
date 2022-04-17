using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class UpperChest : MonoBehaviour
{
    // Start is called before the first frame update
    public GameObject originalCrossHair;
    public GameObject touchCrossHair;
    public GameObject aCamera;
    public GameObject drawer;
    public Text ChestText;
  //  public Text BanText;
    private bool ChestClosed = true;
    private bool Check;
  //  public PickCoin pickCoin;
    private Animator animator;
    private AudioSource sound;
    // Start is called before the first frame update
    void Start()
    {
        //pickCoin = GetComponent<PickCoin>();
        animator = GetComponent<Animator>();
        sound = GetComponent<AudioSource>();

    }

    void Update()
    {
        // check if the sight touches the chest of drawers
        RaycastHit hit;
        Physics.Raycast(aCamera.transform.position, aCamera.transform.forward, out hit);
        // cross hair switch
        if ((hit.transform.gameObject == this.gameObject || // is the hit objet a chest
            hit.transform.gameObject == drawer.gameObject) && hit.distance < 3)
        {
            if (!touchCrossHair.gameObject.activeSelf)
            {
                originalCrossHair.SetActive(false);
                touchCrossHair.SetActive(true);
            }
        }
        else
        {
            if (touchCrossHair.gameObject.activeSelf)
            {
                originalCrossHair.SetActive(true);
                touchCrossHair.SetActive(false);
            }

        }
        // open/close drawer
        if (hit.transform.gameObject == drawer.gameObject && hit.distance < 5)
        {
            if (!ChestText.IsActive())
                ChestText.gameObject.SetActive(true);


            if (Input.GetKeyDown(KeyCode.E))
            {
                StartCoroutine(OpenCloseDrawer());
            }
        }
        else // the focus is not on drawer
        {
            if (ChestText.IsActive())
                ChestText.gameObject.SetActive(false);

        }
    }

    IEnumerator OpenCloseDrawer()
    {
        animator.SetBool("OpenChest", ChestClosed);
        ChestClosed = !ChestClosed;
        sound.PlayDelayed(0.5F);

        yield return new WaitForSeconds(2);

        if (ChestClosed)
            ChestText.text = "Press [E] to open";
        else
            ChestText.text = "Press [E] to close";

    }
}

