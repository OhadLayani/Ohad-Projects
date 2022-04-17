using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SlidingDoor : MonoBehaviour
{
    private Animator animator;
    private AudioSource Sound;
    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
        Sound = GetComponent<AudioSource>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private void OnTriggerEnter(Collider other)
    {
        animator.SetBool("DoorOpens", true);
        Sound.PlayDelayed(0.7f);
    }
    private void OnTriggerExit(Collider other)
    {
        animator.SetBool("DoorOpens", false);
        Sound.PlayDelayed(0.7f);

    }
}
