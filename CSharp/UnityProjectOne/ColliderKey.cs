using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ColliderKey : MonoBehaviour
{
    public GameObject Key;
    private Animator animator;
    public AudioSource sound;
    public AudioSource Locksound;
    public Text Popup;
    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        sound = GetComponent<AudioSource>();
        Locksound = GetComponent<AudioSource>();
        //might need public audiosources per assignment?

    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnTriggerEnter(Collider other)
    {
        if (Key.activeSelf)
        {
            Key.gameObject.SetActive(false);
            animator.SetBool("HaveKey",true);
            animator.SetBool("DoorOpens", true);

            sound.PlayDelayed(0.7F);

        }
        else
        {
            animator.SetBool("HaveKey", false);
            Locksound.PlayDelayed(0.2F);
            StartCoroutine(PopupText());


        }
    }
    public IEnumerator PopupText()
    {
        if (!Popup.IsActive())
        {
            Popup.gameObject.SetActive(true);
        }
        Popup.text = "You need a key to open this";
        yield return new WaitForSeconds(3);
        Popup.gameObject.SetActive(false);
    }
}
