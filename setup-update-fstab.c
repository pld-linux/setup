/*
 * $Id$
 * adds devmode and devgid to usbfs in fstab
 *
 */
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>

void eputs(const char *msg)
{
	write(2, msg, strlen(msg));
}

int main()
{
	char *name = "/etc/fstab";
	char *backup_name = "/etc/fstab.bak";
	char *add = ",devmode=0664,devgid=78";
	
	char *old;
	int i, fd;
	int old_sz;
	struct stat st;

	eputs("Updating /etc/fstab...");
	fd = open(name, O_RDONLY);
	if (fd < 0) {
		eputs("\nError: can't open file\n");
		return 1;
	}
	fstat(fd, &st);
	old = (char *) malloc(st.st_size);
	if (old == NULL) {
		eputs("\nError: malloc failure\n");
		return 1;
	}
	read(fd, old, st.st_size);
	close(fd);
	old_sz = st.st_size;
	
	fd = open(backup_name, O_WRONLY|O_CREAT|O_TRUNC, 0600);
	if (fd < 0) {
		eputs("\nError: can't make backup\n");
		return 2;
	}
	write(fd, old, old_sz);
	close(fd);
	
	// find usbfs
	for (i = 0; i < old_sz; i++) {
		if ( old[i] == 'u' && old[i+1] == 's' && old[i+2] == 'b'
				&& old[i+3] == 'f' && old[i+4] == 's')
			break;
	}
	// find defau(lts)
	for (;i < old_sz; i++) {
		if ( old[i] == 'd' && old[i+1] == 'e' && old[i+2] == 'f' && old[i+3] == 'a' && old[i+4] == 'u' )
			break;
	}
	// find first space
	for (;i < old_sz; i++) {
		if ( old[i] == ' ' || old[i] == '\t' )
			break;
	}
	if ( i >= old_sz ) {
		eputs("\nError: can't find correct usbfs entry\n");
		return 3;
	}
	
	fd = open(name, O_WRONLY|O_CREAT|O_TRUNC);
	if (fd < 0) {
		eputs("\nError: can't open file for writing\n");
		return 4;
	}
	write(fd, old, i);
	write(fd, add, strlen(add));
	write(fd, old + i, old_sz - i);
	close(fd);
	eputs("OK\n");
	
	return 0;
}

